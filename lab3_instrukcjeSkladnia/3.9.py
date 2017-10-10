L = [[],[4],(1,2),[3,4],(5,6,7)]

sumL = list()

for element in L:
    sumL.append(sum(element))

print("Sum of elements in list: ", sumL)