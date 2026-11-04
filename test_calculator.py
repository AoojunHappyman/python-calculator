import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add2(self):
        self.assertEqual(self.calc.add(6,7), 13)

    def test_add3(self):
        self.assertEqual(self.calc.add(6,6), 12)

    def test_sub1(self):
        self.assertEqual(self.calc.subtract(2,1),1)

    def test_sub2(self):
        self.assertEqual(self.calc.subtract(2,2),0)

    def test_multiple1(self):
        self.assertEqual(self.calc.multiply(2,3),6)

    def test_multiple2(self):
        self.assertEqual(self.calc.multiply(5,4),20)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(6,3),2)

    def test_devide2(self):
        self.assertEqual(self.calc.divide(7,7),1)

    def test_mod1(self):
        self.assertEqual(self.calc.modulo(10,3),1)

    def test_mod2(self):
        self.assertEqual(self.calc.modulo(10,4),2)

if __name__ == '__main__':
    unittest.main()