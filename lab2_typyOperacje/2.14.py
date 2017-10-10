line = "Przykladowy tekst do zadania z przedmiotu Python"
allWords = line.split()

maxLenWord = 0
maxWord = ""

for word in allWords:
    if len(word) > maxLenWord:
        maxLenWord = len(word)
        maxWord = word

print("The longest word: " + maxWord)
print("Length of the longest word: " + str(maxLenWord))
