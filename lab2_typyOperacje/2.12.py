line = "Przykladoy tekst do zadania z przedmiotu Python"

initialLetters = ""
terminalLetters = ""

allWords = line.split()

for word in allWords:
    initialLetters = initialLetters + word[0]
    terminalLetters = terminalLetters + word[len(word)-1]


print(initialLetters)
print(terminalLetters)