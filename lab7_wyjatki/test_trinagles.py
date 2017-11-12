#!/usr/bin/python

import unittest
from points import Point
from trinagles import Triangle


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.tr1 = Triangle(1, 1, 5, 1, 1, 4)
        self.tr2 = Triangle(1, 1, 5, 1, 1, 4)

    def test_str(self):
        self.assertEqual(str(self.tr1), "[(1, 1), (5, 1), (1, 4)]")

    def test_repr(self):
        self.assertEqual(repr(self.tr1), "Triangle(1, 1, 5, 1, 1, 4)")

    def test_eq(self):
        self.assertTrue(self.tr1 == self.tr2)

    def test_ne(self):
        self.assertFalse(self.tr1 != self.tr2)

    def test_center(self):
        self.assertEqual(self.tr1.center(), Point(7/3, 2))

    def test_area(self):
        self.assertEqual(self.tr1.area(), 6)

    def test_move(self):
        self.assertEqual(self.tr1.move(2, 2), Triangle(3, 3, 7, 3, 3, 6))
        
    def test_make4(self):
		pass
        # self.assertEqual(self.tr1.make4(), [Triangle(-4, 0, -2, -4, 2, -4),
                                            # Triangle(-4, 0, 2, -4, 1, 1),
                                            # Triangle(-2, -4, 2, -4, 5, 1),
                                            # Triangle(-4, 0, -2, -4, 3, 5)])

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy