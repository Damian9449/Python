#!/usr/bin/python

from numbers import Number

class Frac:
    """Klasa reprezentujaca ulamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.	
		if y == 0:
			raise ValueError("You must change value of denominator")
		else:
			self.x = x
			self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        else:
            return (str(self.x) + "/" + str(self.y))

    def __repr__(self):        # zwraca "Frac(x, y)"
        return ("Frac(" + str(self.x) + "/" + str(self.y) + ")")

    # sprowadzenie do wspolnego mianownika
    def nwd(self, m1, m2):
        while m2 != 0:
            m2, m1 = m1 % m2, m2
        return m1

    def nww(self, a, b):
        m1, m2 = a.y, b.y
        return abs(m1 * m2 / self.nwd(m1, m2))

    def __cmp__(self, other):   # porownywanie
		denominator = self.nww(self, other)
		numerator1 = denominator / self.y * self.x
		numerator2 = denominator / other.y * other.x
		if numerator1 == numerator2:
			return 0
		elif numerator1 > numerator2:
			return 1
		else:
			return -1

    def __add__(self, other):  # frac1+frac2, frac+int
		if isinstance(other, Number):
			return Frac(other) + self
		else:
			denominator = self.nww(self, other)
			numerator1 = denominator / self.y * self.x
			numerator2 = denominator / other.y * other.x
			return Frac(numerator1 + numerator2, denominator)		

    __radd__ = __add__              # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
		if isinstance(other, Number):
			return self - Frac(other)
		else:
			denominator = self.nww(self, other)
			numerator1 = denominator / self.y * self.x
			numerator2 = denominator / other.y * other.x
			return Frac(numerator1 - numerator2, denominator)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
		return Frac(other * self.y - self.x, self.y)

    def __mul__(self, other):     # frac1*frac2, frac*int
		if isinstance(other, Number):
			return self * Frac(other)
		else:
			return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):  # frac1/frac2, frac/int
		if isinstance(other, Number):
			return self / Frac(other)
		else:
			inverted = ~other
			return Frac(self.x * inverted.x, self.y * inverted.y)

    def __rdiv__(self, other): # int/frac
		# tutaj self jest frac, a other jest int!
		return Frac(other * self.y, self.x)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):         # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):       # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return float(self.x)/float(self.y)

