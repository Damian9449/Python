#!/usr/bin/python

from points import Point

class Circle:
    """Klasa reprezentujaca okregi na plaszczyznie."""

    def __init__(self, x=0, y=0, radius=1):
        if (radius < 0) or (type(x) is not (int or float) ) or (type(y) is not (int or float)):
            raise ValueError("zly zestaw danych")
		
        self.pt = Point(x, y)
        self.radius = radius
	
    def __repr__(self):        # "Circle(x, y, radius)"
		return "Circle(" + str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")"  

    def __eq__(self, other):
		if isinstance(other, Circle):
			return ((self.pt == other.pt) and (self.radius == other.radius))
		else:
			raise ValueError("arg musi byc instancja klasy Circle")

    def __ne__(self, other):
		return not self == other

    def area(self):           # pole powierzchni
		from math import pi
		return pi * self.radius * self.radius

    def move(self, x, y):     # przesuniecie o (x, y)
		if ((isinstance(x, int) or isinstance(x, float)) and \
			(isinstance(y, int) or isinstance(y, float))):
			self.pt.x = self.pt.x + x
			self.pt.y = self.pt.y + y
			return Circle(self.pt.x, self.pt.y, self.radius)
		else:
			raise ValueError("zly zestaw danych")
		
    def cover(self, other):   # okrag pokrywajacy oba
		from math import sqrt
		if isinstance(other, Circle):
			wsp_x = (self.pt.x + other.pt.x)/2
			wsp_y = (self.pt.y + other.pt.y)/2
			d = sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)
			radius = self.radius + other.radius + d
			return Circle(wsp_x, wsp_y, radius)
		else:
			raise ValueError("arg musi byc instancja klasy Circle")
			