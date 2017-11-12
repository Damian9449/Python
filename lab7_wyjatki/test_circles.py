#!/usr/bin/python

import unittest
from circles import*
from points import*


class TestCircle(unittest.TestCase):

	def setUp(self):
		self.cr1 = Circle(1, 1, 2)
		self.cr2 = Circle(1, 1, 2)
		self.cr3 = Circle(3, 3, 2)
		self.cr4 = Circle(3, 1, 2)

	def test_repr(self):
		self.assertEqual(repr(self.cr1), "Circle(1, 1, 2)")

	def test_eq(self):
		self.assertTrue(self.cr1 == self.cr2)

	def test_ne(self):
		self.assertFalse(self.cr1 != self.cr2)

	def test_area(self):
		from math import pi
		self.assertEqual(self.cr1.area(), 4*pi)

	def test_move(self):
		self.assertEqual(self.cr1.move(2, 2), self.cr3)
		self.assertRaises(ValueError, self.cr1.move, 2, 'a')
		
	def test_cover(self):
		self.assertEqual(self.cr1.cover(self.cr4), Circle(2, 1, 6))
		self.assertRaises(ValueError, self.cr1.cover, 2)
		
if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
	