L = "Przykladowy teskt do potrzeb zadania"

amountWord = 0

for letter in L:
    if letter.isspace() and letter:
        amountWord = amountWord + 1


print("Amount of word in string: " + str(amountWord+1))
print(L)
