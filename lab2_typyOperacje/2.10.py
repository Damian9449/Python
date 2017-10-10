#!/usr/bin/python
L = "Przykladowy teskt do potrzeb zadania"

amountWord = 0

for letter in L:
    if letter.isspace() and letter:
        amountWord = amountWord + 1

		
print("Tekst: " + L)
print("Amount of word in string: " + str(amountWord+1))

