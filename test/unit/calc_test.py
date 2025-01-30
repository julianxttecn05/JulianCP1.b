import pytest
import unittest

from app.calc import Calculator
from app import util

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(10, 6))
        self.assertEqual(-2, self.calc.substract(256, 258))
        self.assertEqual(-1, self.calc.substract(-1, 0))
        self.assertEqual(0, self.calc.substract(0, 0))
        self.assertRaises(TypeError, self.calc.substract, "0", 0)
    
    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertRaises(TypeError, self.calc.multiply, "0", 0)
    
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, 2, 0)  # División por cero
    
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(1, self.calc.power(-1, 0))
        self.assertEqual(-27, self.calc.power(-3, 3))
        self.assertRaises(TypeError, self.calc.power, "0", 0)
    
@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
