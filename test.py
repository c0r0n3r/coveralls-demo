import unittest

from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_with_zero_input(self):
        assert fibonacci(0) == 0

    def test_fibonacci_with_one_input(self):
        assert fibonacci(1) == 1


if __name__ == '__main__':
    unittest.main()
