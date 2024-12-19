square_height = int(input("Введите высоту квадрата:\n"))
square_width = int(input("Введите ширину квадрата:\n"))

i = 0

while i < square_width:
    if i == 0 or i == square_width - 1:
        print("*" * square_height)
    else:
        print("*" + " " * (square_height - 2) + "*")
    i += 1
