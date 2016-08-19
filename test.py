import unittest

from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_with_zero_input(self):
        assert fibonacci(0) == 0


if __name__ == '__main__':
    unittest.main()
