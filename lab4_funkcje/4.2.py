#!/usr/bin/python

def ruler_fun():
    prompt = "Enter size of ruler : "
    sizeRuler = int(input(prompt))

    tmp1 = sizeRuler
    ruler = "|"

    while tmp1 > 0:
        ruler = ruler + "." * 3 + "|"
        tmp1 = tmp1 - 1

    ruler = ruler + "\n" + "0"

    tmp2 = 1
    while tmp2 < sizeRuler + 1:
        if tmp2 < 10:
            ruler = ruler + " " * 3 + str(tmp2)
        else:
            ruler = ruler + " " * 2 + str(tmp2)
        tmp2 = tmp2 + 1
    return ruler

def rectangle_fun():
    prompt = "Enter width of rectangle : "
    widthRectangle = int(input(prompt))
    tmp1 = widthRectangle
    tmp2 = widthRectangle

    prompt = "Enter height of rectangle : "
    heightRectangle = int(input(prompt))

    rectangle = "+"

    while heightRectangle > 0:
        while tmp1 > 0:
            rectangle = rectangle + "-" * 3 + "+"
            tmp1 = tmp1 - 1

        rectangle = rectangle + "\n" + "|"
        while tmp2 > 0:
            rectangle = rectangle + " " * 3 + "|"
            tmp2 = tmp2 - 1

        rectangle = rectangle + "\n" + "+"

        tmp2 = widthRectangle
        tmp1 = widthRectangle
        heightRectangle = heightRectangle - 1

        if heightRectangle == 0:
            while tmp2 > 0:
                rectangle = rectangle + "-" * 3 + "+"
                tmp2 = tmp2 - 1

    return rectangle


rectangle = rectangle_fun()
ruler = ruler_fun()

print(ruler)
print(rectangle)
