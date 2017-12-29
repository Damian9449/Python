#!/usr/bin/python

import os
from randomNumber import random_number

numberOfNumbers = 50

def swap(L, left, right):
	L[left], L[right] = L[right], L[left]

def shakersort(L, left, right):
    k = right
    sortingStages = []
    
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
        
        sortingStages.append(list(L))
    
    return sortingStages

    
randomNumber = random_number(numberOfNumbers)
allStagesOfSorting = shakersort(randomNumber, 0, len(randomNumber)-1)

for j in range(len(allStagesOfSorting)):
    plik = open('sort'+str(j+1)+'.dat', 'w')
    for i in range(numberOfNumbers):
        plik.writelines(str(i) + " " + str(allStagesOfSorting[j][i]) + "\n")
    plik.close()
    os.system("gnuplot " + 'sort'+str(j+1) +"png.gnu")
