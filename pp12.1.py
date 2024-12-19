start = int(input("Введите начало диапазона:\n"))
end = int(input("Введите конец диапазона:\n"))
list = []

while start <= end:
    list.append(start)
    start += 1

print("Сумма чисел диапазона:", sum(list))
print("Среднее арифметическое:", (sum(list) / len(list)))
