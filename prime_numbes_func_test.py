import unittest

import prime_number_generator as test_func


class PrimeNumberstestCase(unittest.TestCase):
    def test_returns_true(self):
        self.assertEqual(test_func.prime_number_gen(10), [2, 3, 5, 7])
    def test_returns_true(self):
        self.assertEqual(test_func.prime_number_gen(2), [2])

if __name__ == '__main__':
    unittest.main()
