#!/usr/bin/python

from points import Point

class Rectangle:
    """Klasa reprezentujaca prostokat na plaszczyznie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return ("[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), "
                + "(" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]")

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return ("Rectangle (" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), "
                + "(" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")")

    def __eq__(self, other):   # obsluga rect1 == rect2
        return (((self.pt1.x == other.pt1.x) and (self.pt1.y == other.pt1.y) and
            (self.pt2.x == other.pt2.x) and (self.pt2.y == other.pt2.y))
            or
            ((self.pt1.x == other.pt2.x) and (self.pt1.y == other.pt2.y) and
             (self.pt2.x == other.pt1.x) and (self.pt2.y == other.pt1.y)))

    def __ne__(self, other):        # obsluga rect1 != rect2
        return not (((self.pt1.x == other.pt1.x) and (self.pt1.y == other.pt1.y) and
            (self.pt2.x == other.pt2.x) and (self.pt2.y == other.pt2.y))
            or
            ((self.pt1.x == other.pt2.x) and (self.pt1.y == other.pt2.y) and
             (self.pt2.x == other.pt1.x) and (self.pt2.y == other.pt1.y)))

    def center(self):          # zwraca srodek prostokata
        return Point(
            (self.pt1.x + self.pt2.x)/2.0,
            (self.pt1.y + self.pt2.y)/2.0 )

    def area(self):            # pole powierzchni
        return abs( (self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y) )

    def move(self, x, y):       # przesuniecie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)