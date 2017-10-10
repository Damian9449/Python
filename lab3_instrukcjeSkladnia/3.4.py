prompt = "Enter text: "
tmp_text = ""

while tmp_text != "stop":
    tmp_text = input(prompt)

    try:
        number = float(tmp_text)
    except ValueError:                  # kod obslugujacy bledy
        print ("It isn't a number! ")
    else:                               # jesli nie bylo zgloszenia wyjatku
        print("Number: " + str(number) + " ,third power: ", str(number ** 3))