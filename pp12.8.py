import random
import time

random_num = random.randint(1, 500)
user_guess = int(input("Угадайте число от 1 до 500:\n"))
attempt_counter = 0

timer_start = time.time()


while random_num != user_guess:
    if random_num < user_guess:
        user_guess = int(input("Это число меньше\nВведите 0 если надоело угадывать:\n"))
        attempt_counter += 1
    elif user_guess == 0:
        print("Завершение программы...")
        exit()
    elif random_num > user_guess:
        user_guess = int(input("Это число больше\nВведите 0 если надоело угадывать:\n"))
        attempt_counter += 1

timer_stop = time.time()
print(
    "Вы отгадали число!\nИм оказалось",
    random_num,
    "\nВы отгадали число за",
    attempt_counter,
    "попыток за",
    timer_stop - timer_start,
    "секунд.",
)
