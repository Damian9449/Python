#!/usr/bin/python

line = "Przykladoy tekst do zadania z przedmiotu Python"

allWords = line.split()

result = sum(len(x) for x in allWords)

print(result)