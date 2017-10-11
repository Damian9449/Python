#!/usr/bin/python

line = "Przykladoy tekst do zadania z przedmiotu Python"

firstLetters = ""
endLetters = ""

allWords = line.split()

for word in allWords:
    firstLetters = firstLetters + word[0]
    endLetters = endLetters + word[len(word)-1]

print(firstLetters)
print(endLetters)
