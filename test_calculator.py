# https://github.com/zbon0830/lab10-ZB-MJ
# Partner 1: Zachary Bon
# Partner 2: Maxine Johnson
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,5),8)
        self.assertEqual(add( -7, 5), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(12, 4), 8)
        self.assertEqual(add(5, 0), 5)
    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(mul(-2, 4), -8)
        self.assertEqual(mul(0, 100), 0)


    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(3, 10), 10/3)
        self.assertEqual(div(-4, 20), -5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,4)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,100),2)
        self.assertEqual(logarithm(5, 5), 1)
        self.assertEqual(logarithm(2,8),3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-1, -1)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, -1)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))
        self.assertEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()