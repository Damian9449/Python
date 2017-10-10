#!/usr/bin/python

import os
from randomNumber import random_number

def swap(L, left, right):
	L[left], L[right] = L[right], L[left]

def shakersort(L, left, right):
    k = right
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                swap(L, j-1, j)
                k = j
        left = k
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                k = j
        right = k

		
randomNumber = random_number(10)

print("Number before sort: ")
print(randomNumber)

plik = open('sort1.dat', 'w')
for i in range(10):
	plik.writelines(str(i) + " " + str(randomNumber[i]) + "\n")
plik.close()

print("Number after sort")
shakersort(randomNumber, 0, len(randomNumber)-1)
print(randomNumber)

plik = open('sort2.dat', 'w')
for i in range(10):
	plik.writelines(str(i) + " " + str(randomNumber[i]) + "\n")
plik.close()


os.system("gnuplot sort1png.gnu")
os.system("gnuplot sort2png.gnu")
