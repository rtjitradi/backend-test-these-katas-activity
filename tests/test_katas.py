import unittest
import katas
import math  # https://docs.python.org/3/library/math.html
import random  # https://docs.python.org/3/library/random.html

# refer to https://docs.python.org/3/library/unittest.html and https://github.com/rtjitradi/backend-katas-functions-loops/blob/master/tests/test_main.py


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertIsNotNone(katas.add)  # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone
        for _ in range(5):
            x = random.randrange(-500, 500) 
            y = random.randrange(-500, 500)
            self.assertEqual(katas.add(x, y), x + y)

    def test_multiply(self):
        self.assertIsNotNone(katas.multiply)
        self.assertEqual(katas.multiply(2, 2), 4)
        self.assertEqual(katas.multiply(1, -7), -7)
        self.assertEqual(katas.multiply(-10, -8), 80)
        self.assertEqual(katas.multiply(-1, 100), -100)
        for _ in range(5):
            x = random.randrange(-500, 500)
            y = random.randrange(-500, 500)
            self.assertEqual(katas.multiply(x, y), x * y)

    def test_power(self):
        self.assertIsNotNone(katas.power)
        self.assertEqual(katas.power(2, 3), 2 ** 3)
        self.assertEqual(katas.power(-1, 3), -1 ** 3)
        self.assertEqual(katas.power(100, 0), 1)
        for _ in range(50):
            x = random.randrange(-50, 50)
            y = random.randrange(0, 50)
            self.assertEqual(katas.power(x, y), x ** y)

    def test_factorial(self):
        self.assertIsNotNone(katas.factorial)
        self.assertEqual(katas.factorial(4), math.factorial(4))
        for i in range(50):
            self.assertEqual(katas.factorial(i), math.factorial(i))

    def test_fibonacci(self):
        self.assertIsNotNone(katas.fibonacci)
        fibs = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
        for n in range(11):
            self.assertEqual(katas.fibonacci(n), fibs[n])


if __name__ == '__main__':
    unittest.main()
