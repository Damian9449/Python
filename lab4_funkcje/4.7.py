#!/usr/bin/python

L = [1, 2, [3, 4], [5, [6, 7, (8, 9)]], 10, [[11]]]


def flatten(sequence):
    result = []
    for i in range(len(sequence)):
        if isinstance(sequence[i], (list, tuple)):
            result.extend(flatten(sequence[i]))
        else:
            result.append(sequence[i])
    return result


print("Orginal L: ", L)
print("Result L: ", flatten(L))
