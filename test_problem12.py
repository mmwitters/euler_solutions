from unittest import TestCase

from problem12 import prime_factors, num_of_factors

from collections import Counter


class Test(TestCase):
    def test_num_of_factors(self):
        self.assertEqual(4, num_of_factors(10))
        self.assertEqual(2, num_of_factors(3))
        self.assertEqual(6, num_of_factors(28))

    def test_prime_factors(self):
        self.assertEqual(Counter({2: 2}), prime_factors(4))
        self.assertEqual(Counter({2: 1, 5: 1}), prime_factors(10))
        self.assertEqual(Counter({2: 2, 3: 1}), prime_factors(12))
        self.assertEqual(Counter({2: 1}), prime_factors(2))
        self.assertEqual(Counter({2: 4}), prime_factors(16))
