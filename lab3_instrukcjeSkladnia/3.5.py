#!/usr/bin/python

prompt = "Enter size of ruler : "
sizeRuler = int(input(prompt))

tmp1 = sizeRuler
ruler = "|"

while tmp1 > 0:
    ruler = ruler + "." * 3 + "|"
    tmp1 = tmp1 - 1

ruler = ruler + "\n" + "0"

tmp2 = 1
while tmp2 < sizeRuler+1:
    if tmp2 < 10:
        ruler = ruler + " " * 3 + str(tmp2)
    else:
        ruler = ruler + " " * 2 + str(tmp2)
    tmp2 = tmp2 + 1

print(ruler)