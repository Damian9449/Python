import unittest
from points import*

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(2, 3)

    def test_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point (1, 2)")

    def test_eq(self):
        self.assertFalse(self.p1 == self.p2)

    def test_ne(self):
        self.assertTrue(self.p1 != self.p2)

    def test_add(self):
        self.assertEqual((self.p1 + self.p2), Point(3, 5))

    def test_sub(self):
        self.assertEqual((self.p1 - self.p2), Point(-1, -1))

    def test_mul(self):
        self.assertEqual((self.p1 * self.p2), 8)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), -1)

    def test_length(self):
        from math import sqrt
        self.assertEqual(self.p1.length(), sqrt(5))

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
