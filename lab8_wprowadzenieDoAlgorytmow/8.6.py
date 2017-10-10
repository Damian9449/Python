#!/usr/bin/python

# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.


def p(i, j):

    tab = [[0.0 for col in range(i+1)] for row in range(j+1)]
    tab[0][0] = 0.5

    for t in range(1, j+1):
        tab[t][0] = 1.0

    for m in range(1, i+1):
        for k in range(1, j+1):
            tab[k][m] = 0.5 * (tab[k - 1][m] + tab[k][m - 1])

    return tab[j][i]


def p_rek(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    else:
        return 0.5 * (p_rek(i-1, j) + p_rek(i, j-1))


print("Recursive version: ", p_rek(2, 5))
print("Dynamic version: ", p(2, 5))
