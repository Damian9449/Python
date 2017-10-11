#!/usr/bin/python

def add_poly(poly1, poly2):             # poly1(x) + poly2(x)
    tmp = 0
    min_value = min(len(poly1), len(poly2))
    result = []

    while tmp < min_value:
        result.append(poly1[tmp] + poly2[tmp])
        tmp = tmp + 1

    while tmp < len(poly1):
        result.append(poly1[tmp])
        tmp = tmp + 1

    while tmp < len(poly2):
        result.append(poly2[tmp])
        tmp = tmp + 1

    return result

def sub_poly(poly1, poly2):             # poly1(x) - poly2(x)
    tmp = 0
    min_value = min(len(poly1), len(poly2))
    result = []

    while tmp < min_value:
        result.append(poly1[tmp] - poly2[tmp])
        tmp = tmp + 1

    while tmp < len(poly1):
        result.append(poly1[tmp])
        tmp = tmp + 1

    while tmp < len(poly2):
        result.append(poly2[tmp])
        tmp = tmp + 1

    return result

def mul_poly(poly1, poly2):                 # poly1(x) * poly2(x)
    degreeFirstPoly = len(poly1)
    degreeSecondPoly = len(poly2)
    degreeResultPoly = degreeFirstPoly + degreeSecondPoly - 1
    i = 0
    j = 0
    result = [0] * degreeResultPoly

    while len(poly1) < degreeResultPoly:
        poly1.append(0)

    while len(poly2) < degreeResultPoly:
        poly2.append(0)

    for i in range(degreeFirstPoly):
        for j in range(degreeSecondPoly):
            result[i+j] += poly1[i]*poly2[j]

    return result

def is_zero(poly):                      # bool, [0], [0,0], itp.
    for ele in poly:
        if ele != 0:
            return False

    return True

def cmp_poly(poly1, poly2):             # bool, porownywanie
    tmp = 0
    min_value = min(len(poly1), len(poly2))

    while tmp < min_value:
        if poly1[tmp] != poly2[tmp]:
            return False
        tmp = tmp + 1

    while tmp < len(poly1):
        if poly1[tmp] != 0:
            return False
        tmp = tmp + 1

    while tmp < len(poly2):
        if poly2[tmp] != 0:
            return False
        tmp = tmp + 1

    return True

def eval_poly(poly, x0):                # poly(x0), algorytm Hornera

    result = poly[len(poly)-1]

    for i in range(len(poly)-2,-1,-1):
        result = result * x0 + poly[i]

    return result

def combine_poly(poly1, poly2):         # poly1(poly2(x)), trudne!

    result = [0] * len(poly2) * poly1[len(poly1)-1] * 2

    for i in range(len(poly1)):
        if i is 0:
            result[0] = poly1[0]

        if i > 0:
            tmp = pow_poly(poly2, i)
            for j in range(len(tmp)):
                result[j] += tmp[j] * poly1[i]

    for i in range(len(result)-1, 0, -1):
        if result[i] == 0:
            del result[i]
        else:
            return result

def pow_poly(poly, n):                  # poly(x) ** n

    if n is 1:
        return poly

    elif n > 1:
        result = mul_poly(poly, poly)

    for i in range(n-2):
         result = mul_poly(result, poly)

    for i in range(len(result)-1, 0, -1):
        if result[i] == 0:
            del result[i]
        else:
            return result

def diff_poly(poly):                    # pochodna wielomianu
    degreeResult = len(poly)-1
    result = [0]*degreeResult

    for i in range(len(poly)-1, 0, -1):
        result[i-1] = poly[i]*degreeResult
        degreeResult = degreeResult - 1

    return result
