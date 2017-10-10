#!/usr/bin/python

import unittest
from polys import*

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [5, 1, 2, 3]     
        self.p2 = [2, 1]   
        self.p3 = 3

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [7, 2, 2, 3])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [3, 0, 2, 3])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [10, 7, 5, 8, 3])

    def test_is_zero(self):
        self.assertFalse(is_zero(self.p1))

    def test_cmp_poly(self):
        self.assertFalse(cmp_poly(self.p1, self.p2))

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, self.p3), 107)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p1, self.p2), [39, 45, 20, 3])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1, self.p3), [125, 75, 165, 286, 156, 201, 179, 63, 54, 27])

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1, 4, 9])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy