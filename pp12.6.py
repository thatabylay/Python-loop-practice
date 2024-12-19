while True:
    sum = float(input("Введите сумму в теңге:\n"))
    conversion_choice = input(
        "Введите валюту, в которую нужно конвертировать деньги:\nrub - конвертация в рубли\nusd - конвертация в доллары\neur - конвертация в евро\nfvb - конвертация в ви-баксы\nstop - остановка программы\n"
    )

    if "rub" in conversion_choice.lower():
        print((sum / 5), "рублей")
    elif "usd" in conversion_choice.lower():
        print((sum / 480), "долларов")
    elif "eur" in conversion_choice.lower():
        print((sum / 500), "евро")
    elif "fvb" in conversion_choice.lower():
        print((sum / 4.8), "вибаксов")
    elif "stop" in conversion_choice.lower():
        print("завершение программы...")
        False
        exit
    else:
        print("такой команды не существует")
