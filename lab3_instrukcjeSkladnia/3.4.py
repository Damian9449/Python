#!/usr/bin/python

prompt = "Enter text: "
tmp_text = input(prompt)

while tmp_text != "stop":

    try:
        number = float(tmp_text)
    except ValueError:                  # kod obslugujacy bledy
        print ("It isn't a number! ")
    else:                               # jesli nie bylo zgloszenia wyjatku
        print("Number: " + str(number) + " ,third power: ", str(number ** 3))