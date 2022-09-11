# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def GetKoordinates(x):
    a = [0] * x
    for i in range(x):
        check_number = False
        while not check_number:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                check_number = True
                if a[i] == 0:
                    check_number = False
                    print("Координата не может быть равна 0 ")
            except ValueError:
                print("Некорректный ввод координат!")
    return a


def checkCoordinates(xy):
    quarter_number = 4
    if xy[0] > 0 and xy[1] > 0:
        quarter_number = 1
    elif xy[0] < 0 and xy[1] > 0:
        quarter_number = 2
    elif xy[0] < 0 and xy[1] < 0:
        quarter_number = 3
    print(f"Координаты точки находятся в {quarter_number} четверти")


koordinate = GetKoordinates(2)
checkCoordinates(koordinate)