# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input("Введите номер четверти (от 1 до 4): "))
if number == 1:
    print(f"Допустимые значения для {number} четверти: x > 0, y > 0")
elif number == 2:
    print(f"Допустимые значения для {number} четверти: x < 0, y > 0")
elif number == 3:
    print(f"Допустимые значения для {number} четверти: x < 0, y < 0")
elif number == 4:
    print(f"Допустимые значения для {number} четверти: x > 0, y < 0")
else:
    print("Неправильно ввели номер четверти прямоугольной системы координат!")