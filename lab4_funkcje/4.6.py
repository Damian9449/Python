#!/usr/bin/python

L = [1, 2, [3, 4], (1, 2), [1, [2, 3, (2, 5)]], 8]


def sum_seq(sequence):
    if len(sequence) == 0:
        return 0
    else:
        if isinstance(sequence[0], (list, tuple)):
            return sum_seq(sequence[0]) + sum_seq(sequence[1:])
        else:
            return sequence[0] + sum_seq(sequence[1:])


print("Result: ", sum_seq(L))
