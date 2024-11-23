import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(4, -3), 0.015625)
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(2, -3), 0.125)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)
        
        # Corrected edge case for division by zero
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()

