import unittest
from rectangles import*

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(1, 1, 4, 3)
        self.rect2 = Rectangle(1, 1, 4, 3)

    def test_str(self):
        self.assertEqual(str(self.rect1), "[(1, 1), (4, 3)]")

    def test_repr(self):
        self.assertEqual(repr(self.rect1), "Rectangle (1, 1), (4, 3)")

    def test_eq(self):
        self.assertTrue(self.rect1 == self.rect2)

    def test_ne(self):
        self.assertFalse(self.rect1 != self.rect2)

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2.5, 2.0))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 6)

    def test_move(self):
        self.assertEqual(self.rect1.move(2, 2), Rectangle(3, 3, 6, 5))


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy