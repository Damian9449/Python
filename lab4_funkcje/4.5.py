L = [1, 2, 3, 4, 5, 6, 7, 8]

def odwracanie_iter(L, left, right):
    maxIndex = right
    numberIterations = int((right - left + 1)/2)
    for i in range(left, left + numberIterations):
        tmp = L[maxIndex]
        L[maxIndex] = L[i]
        L[i] = tmp
        maxIndex -= 1


def odwracanie_rek(l, left, right):
    if left < int((right - left + 1)/2 + left):
        l[left], l[right] = l[right], l[left]
        odwracanie_rek(l, left+1, right-1)

odwracanie_rek(L, 2, 7)
print("Inversed elements ( index: 2 - 5 ): ", L)

odwracanie_iter(L, 2, 7)
print("Inversed elements ( index: 2 - 5 ): ", L)
