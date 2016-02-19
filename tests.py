import unittest

from engine import SuperFormatter


class TestSuperFormatterMethods(unittest.TestCase):
    """tests."""

    def test_basic(self):
        sf = SuperFormatter()
        self.assertEqual(
            sf.format('a is {a}', a="A"),
            "a is A"
        )

    def test_repeat_list(self):
        sf = SuperFormatter()
        self.assertEqual(
            sf.format('''Table of contents:
{chapters:repeat:Chapter {{item}}
}''', chapters=["I", "II", "III", "IV"]),
            '''Table of contents:
Chapter I
Chapter II
Chapter III
Chapter IV
'''
        )

    def test_repeat_dict(self):
        sf = SuperFormatter()
        self.assertEqual(
            sf.format(
                '''Books:

{books:repeat:"{{item[1]}}" by {{item[0]}}
----
}''',
                books={
                    'Victor Hugo': 'Notre Dame de Paris',
                    'Joseph Conrad': 'Lord Jim',
                }),
            '''Books:

"Notre Dame de Paris" by Victor Hugo
----
"Lord Jim" by Joseph Conrad
----
'''
        )

    def test_call(self):
        sf = SuperFormatter()
        self.assertEqual(
            sf.format('My name is {name.upper:call}', name="eric"),
            'My name is ERIC'
        )

    def test_if_static(self):
        sf = SuperFormatter()
        self.assertEqual(
            sf.format('Action: Back / Logout {manager:if:/ Delete}', manager=True),
            'Action: Back / Logout / Delete'
        )

    def test_if_with_fields(self):
        sf = SuperFormatter()
        self.assertEqual(
            sf.format('Action: Back / Logout {manager:if:/ Delete {id}}', manager=False, id=34),
            'Action: Back / Logout / Delete 34'
        )


if __name__ == '__main__':
    unittest.main()
