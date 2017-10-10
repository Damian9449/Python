#!/usr/bin/python

def heron(a, b, c):
    """Obliczanie pola powierzchni trojkata za pomoca wzoru
    Herona. Dlugosci bokow trojkata wynosza a, b, c."""

    from math import sqrt
    L = [a, b, c]
    L.sort()

    if L[0] + L[1] <= L[2]:
        raise ValueError("I can't calculate area of this triangle")
	
	print(a, b, c)
	
    p = (a + b + c) / 2.0
	
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return area


print("Area: ", heron(5, 2, 6))