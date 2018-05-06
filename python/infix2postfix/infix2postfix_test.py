import unittest
from infix2postfix import infix2postfix

class TestInfix2Postfix(unittest.TestCase):

    def test_infix2postfix(self):
        infix = 'a+b*c+(d*e+f)*g'
        postfix = 'abc*+de*f+g*+'
        self.assertEqual(postfix, infix2postfix(infix))


if __name__ == '__main__':
    unittest.main()
