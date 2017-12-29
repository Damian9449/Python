#!/usr/bin/python

def heron(a, b, c):
    """Obliczanie pola powierzchni trojkata za pomoca wzoru
    Herona. Dlugosci bokow trojkata wynosza a, b, c."""
    from math import sqrt

    
    if a + b > c and \
       a + c > b and \
       b + c > a:
       
        p = (a + b + c) / 2.0
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        return area
    else:
        raise ValueError("I can't calculate area of this triangle")


print("Area: ", heron(6, 2, 6))

