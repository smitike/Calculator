import unittest
from calculator import infix_to_postfix, calculate

class TestCalculator(unittest.TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix('(5+2)*3'), '5 2 + 3 *')
        self.assertEqual(infix_to_postfix('5+2*3'), '5 2 3 * +')

    def test_calculate(self):
        self.assertEqual(calculate('(5+2)*3'), 21.0)
        self.assertEqual(calculate('5+2*3'), 11.0)
    print('works!')
if __name__ == '__main__':
    unittest.main()