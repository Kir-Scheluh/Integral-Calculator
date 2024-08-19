while True:
    func = input("Введите функцию: ")

    lower_limit = input("Введите нижний предел: ")
    upper_limit = input("Введите верхний предел: ")

    option = input("Меню:\n"
                   "1. - Метод Симпсона\n"
                   "2. - Метод трапеций\n"
                   "3. - Метод прямоугольников\n"
                   "4. - Метод Монте-Карло\n"
                   "0. - Выход\n")
    match option:
        case "1":
            number_of_partitions = int(input("Введите целым числом количество разбиений: "))
        case "2":
            number_of_partitions = int(input("Введите целым числом количество разбиений: "))
        case "3":
            number_of_partitions = int(input("Введите целым числом количество разбиений: "))
        case "4":
            number_of_partitions = int(input("Введите целым числом количество испытаний: "))
        case "0":
            break
        case _:
            print(f"Неизвестная команда: {option}")