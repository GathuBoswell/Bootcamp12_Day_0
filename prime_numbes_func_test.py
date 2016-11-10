import unittest

import prime_number_generator as test_func


class PrimeNumbersTestCase(unittest.TestCase):

    def test_returns_true1(self):
        self.assertEqual(test_func.prime_number_gen(10), [2, 3, 5, 7])

    def test_returns_true2(self):
        self.assertEqual(test_func.prime_number_gen(2), [2])

    def test_returns_true_if_n_is_prime(self):
        self.assertEqual(test_func.prime_number_gen(5), [2, 3, 5])

    def test_negative_input(self):
        self.assertEqual(test_func.prime_number_gen(-1), 'Only Positve Numbers allowed')

    def test_input_0(self):
        self.assertEqual(test_func.prime_number_gen(0), [])

    def test_input_0(self):
        self.assertEqual(test_func.prime_number_gen(1), [])

    def test_input_is_not_empty_string(self):
        self.assertEqual(test_func.prime_number_gen(''), 'Only Numbers allowed')

    def test_input_is_not_list(self):
        self.assertEqual(test_func.prime_number_gen([]), 'Only Numbers allowed')

    def test_input_is_not_dictionary(self):
        self.assertEqual(test_func.prime_number_gen({}), 'Only Numbers allowed')

    def test_input_is_not_sting(self):
        self.assertEqual(test_func.prime_number_gen('This is'), 'Only Numbers allowed')