#!/usr/bin/python

def Fibonaci_iter(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n > 1):
        fn = 0
        fn1 = 1
        fn2 = 1

        while n > 2:
            fn = fn1 + fn2
            fn1 = fn2
            fn2 = fn
            n = n - 1

        return fn


print(Fibonaci_iter(4))