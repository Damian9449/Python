L = "MCDCDXLXLXVI"


def roman2int(number):
    tmp = 0
    result = 0
    D = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    while tmp < len(number)-1:

        if D[number[tmp]] >= D[number[tmp + 1]]:
            result = result + D[number[tmp]]
        else:
            result = result + (D[number[tmp + 1]] - D[number[tmp]])
            tmp = tmp + 1

        tmp = tmp + 1
    result = result + D[number[tmp]]

    return result

print("Roman: ", L, "Arabic: ", roman2int(L))
