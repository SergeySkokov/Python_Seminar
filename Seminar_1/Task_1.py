# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


def CheckForCorrectionNumbers(inputNumbers):
    check_number = False
    while not check_number:
        try:
            number = int(input(f"{inputNumbers}"))
            check_number = True
        except ValueError:
            print("Некорректный номер")
    return number


def checkDayWeek(day):
    if 6 <= day <= 7:
        print("Выходной день")
    elif 0 < day < 6:
        print("Будний день")
    else:
        print("Число не является одним из дней недели")


number_day = CheckForCorrectionNumbers("Введите день недели (цифру от 1 до 7): ")
checkDayWeek(number_day)
