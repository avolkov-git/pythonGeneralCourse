# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def my_func_cycle(x, y):
    inverse_y = y * (-1)
    tmp_x = x

    for index in range(inverse_y - 1):
        tmp_x = tmp_x * x

    return 1 / tmp_x


def my_func(x, y):
    return x**y


user_x = None
user_y = None

while True:
    try:
        user_x = int(input('Введите натуральное число X: '))
    except ValueError:
        print('Вы ввели не число!')

    if (user_x % 1) == 0 and user_x > 0:
        break
    else:
        print('Число должно быть натуральным')

while True:
    try:
        user_y = int(input('Введите число целое отрицательное число Y: '))
    except ValueError:
        print('Вы ввели не число!')

    if (user_y % 1) == 0 and user_y < 0:
        break
    else:
        print('Число должно быть целое отрицательное')

result = my_func_cycle(user_x, user_y)
print(f'Результат вычисления выражения {user_x}^({user_y}): {result}')
result = my_func(user_x, user_y)
print(f'Результат вычисления выражения {user_x}^({user_y}): {result}')
