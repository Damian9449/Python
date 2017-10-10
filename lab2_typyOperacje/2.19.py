#!/usr/bin/python

L = [1, 22, 43, 456, 21, 123, 999, 4]
result = ""

for tmp in L:
    result = result + str(tmp).zfill(3) + " "

print(result)