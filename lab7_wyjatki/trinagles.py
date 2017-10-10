from points import Point


class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return ("[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), "
                + "(" + str(self.pt2.x) + ", " + str(self.pt2.y) + "), "
                + "(" + str(self.pt3.x) + ", " + str(self.pt3.y) + ")]")

    def __repr__(self):         # "Triangle(x1, y1, x2, y2, x3, y3)"
        return ("Triangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", "
                + str(self.pt2.x) + ", " + str(self.pt2.y) + ", "
                + str(self.pt3.x) + ", " + str(self.pt3.y) + ")")

    def __eq__(self, other):    # obsługa tr1 == tr2
        return (
            ((self.pt1 == other.pt1) and (self.pt2 == other.pt2) and (self.pt3 == other.pt3)) or
            ((self.pt1 == other.pt2) and (self.pt2 == other.pt1) and (self.pt3 == other.pt3)) or
            ((self.pt1 == other.pt2) and (self.pt2 == other.pt3) and (self.pt3 == other.pt1)) or
            ((self.pt1 == other.pt1) and (self.pt2 == other.pt3) and (self.pt3 == other.pt2)) or
            ((self.pt1 == other.pt3) and (self.pt2 == other.pt1) and (self.pt3 == other.pt2)) or
            ((self.pt1 == other.pt3) and (self.pt2 == other.pt2) and (self.pt3 == other.pt1))
            )

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def triangleIsOk(self):
        if self.pt1 == self.pt2 or self.pt1 == self.pt3 or self.pt2 == self.pt3:
            raise ValueError("You must enter 3 different points ")

    def center(self):           # zwraca środek trójkąta
        self.triangleIsOk()
        return Point((self.pt1.x + self.pt2.x + self.pt3.x)/3,
                     (self.pt1.y + self.pt2.y + self.pt3.y)/3)

    def area(self):             # pole powierzchni
        from math import sqrt, pow
        self.triangleIsOk()
        a = sqrt(pow(self.pt1.x - self.pt2.x, 2) + pow(self.pt1.y - self.pt2.y, 2))
        b = sqrt(pow(self.pt2.x - self.pt3.x, 2) + pow(self.pt2.y - self.pt3.y, 2))
        c = sqrt(pow(self.pt1.x - self.pt3.x, 2) + pow(self.pt1.y - self.pt3.y, 2))
        p = (a + b + c) / 2
        pole = sqrt(p*(p-a)*(p-b)*(p-c))
        return pole

    def move(self, x, y):       # przesunięcie o (x, y)
        self.triangleIsOk()
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y,
                        self.pt3.x + x, self.pt3.y + y)

    def make4(self):            # zwraca listę czterech mniejszych
        self.triangleIsOk()
        a = Point(self.pt1.x - self.pt2.x, self.pt1.y - self.pt2.y)
        b = Point(self.pt1.x - self.pt3.x, self.pt1.y - self.pt3.y)
        c = Point(self.pt2.x - self.pt3.x, self.pt2.y - self.pt3.y)
        L = list()
        L.append(Triangle(a.x, a.y, b.x, b.y, c.x, c.y))
        L.append(Triangle(a.x, a.y, c.x, c.y, self.pt1.x, self.pt1.y))
        L.append(Triangle(b.x, b.y, c.x, c.y, self.pt2.x, self.pt2.y))
        L.append(Triangle(a.x, a.y, b.x, b.y, self.pt3.x, self.pt3.y))
        return L