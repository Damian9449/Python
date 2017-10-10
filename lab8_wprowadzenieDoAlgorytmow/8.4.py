def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""

    from math import sqrt, pow
    L = [a, b, c]
    L.sort()

    if L[0] + L[1] < L[2]:
        raise ValueError("I can't calculate area of this triangle")

    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return area


print("Area: ", heron(5, 2, 6))