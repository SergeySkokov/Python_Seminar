# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def CheckForCorrectionNumbers(inputNumbers):
    check_number = False
    while not check_number:
        try:
            number = int(input(f"{inputNumbers}"))
            check_number = True
        except ValueError:
            print("Число должно быть целым ")
    return number


def mult(num):
    if num == 1:
        return 1
    else:
        return num * mult(num - 1)


number = CheckForCorrectionNumbers("Введите число: ")

list = []
for i in range(1, number + 1):
    list.append(mult(i))

print(f"Произведения чисел от 1 до {number}:  {list}")