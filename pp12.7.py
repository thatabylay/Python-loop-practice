start = int(input("Введите начало диапазона:\n"))
end = int(input("Введите конец диапазона:\n"))
num_list = []

i = 0

while start <= end:
    num_list.append(start)
    start += 1

num = int(input("Введите число:\n"))

while i < len(num_list):
    if num_list[i] == num:
        num_list[i] = "!", num, "!"
        i += 1
    else:
        i += 1

num = str(num)
num_list = str(num_list)

while True:
    if num in num_list:
        print(num_list)
        break
    else:
        num = input("Число не входит в диапазон. Введите число повторно:\n")
        num_list.replace(num, f"!{num}!")
        continue
