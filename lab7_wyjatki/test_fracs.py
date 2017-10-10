#!/usr/bin/python

import unittest
from fracs import*

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.fracs1 = Frac(1, 0)
        self.fracs2 = Frac(1, 4)
        self.fracs3 = Frac(1, 1)
        self.fracs4 = Frac(2, 5)
        self.fracs5 = Frac(3, 1)

    def test_add(self):
        self.assertRaises(ValueError, self.fracs1.__add__,  self.fracs2)
        self.assertEqual(self.fracs2.__add__(self.fracs3), Frac(5, 4))

    def test_cmp(self):
        self.assertEqual(self.fracs2.__cmp__(self.fracs4), -1)
        self.assertEqual(self.fracs2.__cmp__(self.fracs2), 0)
        self.assertEqual(self.fracs4.__cmp__(self.fracs2), 1)

    def test_lt(self):
        self.assertTrue(self.fracs2 < self.fracs4)

    def test_gt(self):
        self.assertFalse(self.fracs2 > self.fracs4)

    def test_eq(self):
        self.assertTrue(self.fracs2 == self.fracs2)

    def test_str(self):
        self.assertEqual(str(self.fracs5), "3")
        self.assertEqual(str(self.fracs4), "2/5")

    def test_repr(self):
        self.assertEqual(repr(self.fracs4), "Frac(2/5)")

    def test_sub(self):
        self.assertRaises(ValueError, self.fracs1.__sub__, self.fracs2)
        self.assertEqual(self.fracs4.__sub__(self.fracs2), Frac(3, 20))

    def test_rsub(self):
        self.assertRaises( ValueError, self.fracs1.__sub__, self.fracs2 )
        self.assertEqual(( 3 - Frac(2, 5) ), Frac(13, 5))

    def test_mul(self):
        self.assertRaises(ValueError, self.fracs1.__mul__, self.fracs2)
        self.assertRaises(ValueError, self.fracs2.__mul__, self.fracs1)
        self.assertEqual(self.fracs4.__mul__(self.fracs2), Frac(2, 20))

    def test_div(self):
        self.assertRaises(ValueError, self.fracs1.__div__, self.fracs2)
        self.assertRaises(ValueError, self.fracs2.__div__, self.fracs1)
        self.assertEqual(self.fracs4.__div__(self.fracs2), Frac(8, 5))

    def test_rdiv(self):
        self.assertRaises(ValueError, self.fracs1.__rdiv__, self.fracs2)
        self.assertEqual(self.fracs4.__rdiv__(3), Frac(15, 2) )

    def test_pos(self):
        self.assertEqual(self.fracs2.__pos__(), Frac(1, 4))

    def test_neg(self):
        self.assertEqual(self.fracs2.__neg__(), Frac(-1, 4))

    def test_invert(self):
        self.assertEqual(self.fracs4.__invert__(), Frac(5, 2))

    def test_float(self):
        self.assertEqual(self.fracs4.__float__(), 0.4)


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy