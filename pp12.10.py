square_height = int(input("Введите высоту квадрата\n"))
square_width = int(input("Введите ширину квадрата\n"))

row = 0

while row < square_height:
    row += 1
    print("*" * square_width)
