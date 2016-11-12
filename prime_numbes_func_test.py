import unittest

import prime_number_generator as test_func


class PrimeNumbersTestCase(unittest.TestCase):
    def test_returns_true1(self):
        """
         test if result produce is the correct one
        """
        self.assertEqual(test_func.prime_number_gen(10), [2, 3, 5, 7])

    def test_returns_true2(self):
        """
         test if result produce is the correct one
        """
        self.assertEqual(test_func.prime_number_gen(2), [2])

    def test_includes_n_if_n_is_prime(self):
        """
         test if n is included in the result list in n is a prime number
        """
        self.assertEqual(test_func.prime_number_gen(5), [2, 3, 5])

    def test_negative_input(self):
        """
         test if negative numbers are caught as not allowed
        """
        self.assertEqual(test_func.prime_number_gen(-1), 'Only Positve Numbers allowed')

    def test_input_0(self):
        """
         test if n = 0, an empty list is returned
        """
        self.assertEqual(test_func.prime_number_gen(0), [])

    def test_input_1(self):
        """
           test if n = 1, an empty list is returned
        """
        self.assertEqual(test_func.prime_number_gen(1), [])

    def test_input_is_not_empty_string(self):
        """
           test if input is empty string a return message, 'only numbers allowed' is returned
        """
        self.assertEqual(test_func.prime_number_gen('The prime number'), 'Only Numbers allowed')

    def test_input_is_not_list(self):
        """
            test if input is a list a return message, 'only numbers allowed' is returned
         """
        self.assertEqual(test_func.prime_number_gen([]), 'Only Numbers allowed')

    def test_input_is_not_dictionary(self):
        """
            test if input is dictionary a return message, 'only numbers allowed' is returned
         """
        self.assertEqual(test_func.prime_number_gen({}), 'Only Numbers allowed')

    def test_input_is_not_tuple(self):
        """
            test if input is tuple a return message, 'only numbers allowed' is returned
         """
        self.assertEqual(test_func.prime_number_gen((45,)), 'Only Numbers allowed')

    def test_input_is_not_sting(self):
        """
            test if input is None a return message, 'only numbers allowed' is returned
         """
        self.assertEqual(test_func.prime_number_gen(None), 'Only Numbers allowed')
