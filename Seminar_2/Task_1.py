# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 0,56 -> 11

def CheckForCorrectionNumbers(inputNumbers):
    check_number = False
    while not check_number:
        try:
            number = float(input(f"{inputNumbers}"))
            check_number = True
        except ValueError:
            print("Некорректные данные!")
    return number


def sumDigitals(digit):
    sum = 0
    for i in str(digit):
        if i != ".":
            sum += int(i)
    return sum


num = CheckForCorrectionNumbers("Введите число: ")

print(f"Сумма цифр = {sumDigitals(num)}")