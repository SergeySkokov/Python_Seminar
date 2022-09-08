# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def GetCoordinates(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        check_number = False
        while not check_number:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                check_number = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = GetCoordinates(2)
print("Введите координаты точки В")
pointB = GetCoordinates(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")