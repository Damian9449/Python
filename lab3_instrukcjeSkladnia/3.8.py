#!/usr/bin/python

L1 = [6, 2, 3, 4, 5, 1]
L2 = [4, 5, 9, 7, 8, 6]

L1.sort()
L2.sort()

tmp1, tmp2 = 0, 0
mergeList = list()
commonList = list()

print("First list: ", L1)
print("Second list: ", L2)

while (tmp1 != len(L1)) and (tmp2 != len(L2)):
    if L1[tmp1] == L2[tmp2]:
        commonList.append(L1[tmp1])
        tmp1 = tmp1 + 1
    elif  L1[tmp1] < L2[tmp2]:
        mergeList.append(L1[tmp1])
        tmp1 = tmp1 + 1
    elif L1[tmp1] > L2[tmp2]:
        mergeList.append(L2[tmp2])
        tmp2 = tmp2 + 1

while (tmp1 != len(L1)):
    mergeList.append(L1[tmp1])
    tmp1 = tmp1 + 1

while (tmp2 != len(L2)):
    mergeList.append(L2[tmp2])
    tmp2 = tmp2 + 1

print("Common elements lists: ", commonList)
print("All elements in lists: ", mergeList)
