n = int(input("Введите число которому нужно посчитать факториал\n"))
i = 1

while n > 1:
    i *= n
    n -= 1

print(i)
