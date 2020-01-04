import unittest
from peano import *

class TestPeano(unittest.TestCase):

    def test_addition(self):
        print(0)
        self.assertEqual(calc(add, 2, 2), 4)

    def test_substraction(self):
        self.assertEqual(calc(sub, 2, 2), 0)

    def test_multiplication(self):
        self.assertEqual(calc(mult, 4, 4), 16)

if __name__ == "__main__":
    unittest.main()
