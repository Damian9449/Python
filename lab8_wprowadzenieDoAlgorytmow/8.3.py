from random import random
from math import sqrt
from math import pi

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    inside = 0
    for i in range(0, n):
        x = random()
        y = random()
        if sqrt(x * x + y * y) <= 1:
            inside += 1
    pi = 4 * inside / n
    return pi


tmp = calc_pi(1)
print("For 1 points, pi is: " + str(tmp) + " error is: " + str(abs(pi - tmp)) )
tmp = calc_pi(10)
print("For 10 points, pi is: " + str(tmp) + " error is: " + str(abs(pi - tmp)) )
tmp = calc_pi(100)
print("For 100 points, pi is: " + str(tmp) + " error is: " + str(abs(pi - tmp)) )
tmp = calc_pi(1000)
print("For 1000 points, pi is: " + str(tmp) + " error is: " + str(abs(pi - tmp)) )
tmp = calc_pi(10000)
print("For 10000 points, pi is: " + str(tmp) + " error is: " + str(abs(pi - tmp)) )
tmp = calc_pi(100000)
print("For 100000 points, pi is: " + str(tmp) + " error is: " + str(abs(pi - tmp)) )
tmp = calc_pi(1000000)
print("For 1000000 points, pi is: " + str(tmp) + " error is: " + str(abs(pi - tmp)) )
