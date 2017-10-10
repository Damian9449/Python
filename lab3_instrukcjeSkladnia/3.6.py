prompt = "Enter width of rectangle : "
widthRectangle = int(input(prompt))
tmp1 = widthRectangle
tmp2 = widthRectangle

prompt = "Enter height of rectangle : "
heightRectangle = int(input(prompt))

rectangle = "+"

while heightRectangle > 0:
    while tmp1 > 0:
        rectangle = rectangle + "-"*3 + "+"
        tmp1 = tmp1 - 1

    rectangle = rectangle + "\n" + "|"
    while tmp2 > 0:
        rectangle = rectangle + " "*3 + "|"
        tmp2 = tmp2 - 1

    rectangle = rectangle + "\n" + "+"

    tmp2 = widthRectangle
    tmp1 = widthRectangle
    heightRectangle = heightRectangle - 1

    if heightRectangle == 0:
        while tmp2 > 0:
            rectangle = rectangle + "-" * 3 + "+"
            tmp2 = tmp2 - 1

print(rectangle)