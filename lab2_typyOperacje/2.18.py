#!/usr/bin/python

number = 12300250104050806987
strNumber = str(number)

amountZero = 0

for num in strNumber:
    if num == "0" :
        amountZero = amountZero + 1

print("Amount zero in " + str(strNumber) + " is: " + str(amountZero))
