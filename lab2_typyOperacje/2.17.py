#!/usr/bin/python

line = "Przykladowy tekst do zadania z przedmiotu Python"
allWords = line.split()

print(allWords)

sortedListAlp = sorted(allWords)
sortedListLen = sorted(allWords, key=len)

print("Word sorted alphabetically: ")
print(sortedListAlp)

print("Words sorted by their length: ")
print(sortedListLen)
