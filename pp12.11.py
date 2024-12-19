square_length = int(input("Введите длину стороны квадрата:\n"))
i = 0

while i < square_length:
    if i == 0 or i == square_length - 1:
        print(square_length * "*")
    else:
        print("*" + " " * (square_length - 2) + "*")
    i += 1
