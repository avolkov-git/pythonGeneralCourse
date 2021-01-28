# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.
def my_func(a, b, c):

    arg_list = [a, b, c]
    arg_list.sort(reverse=True)

    result = arg_list[0] + arg_list[1]

    return result


num_a = None
num_b = None
num_c = None

while num_a is None:
    try:
        num_a = int(input('Введите первое число: '))
    except ValueError:
        print('Вы ввели не число')

while num_b is None:
    try:
        num_b = int(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели не число')

while num_c is None:
    try:
        num_c = int(input('Введите третье число: '))
    except ValueError:
        print('Вы ввели не число')

numbers_sum = my_func(num_a, num_b, num_c)
print(f'Сумма двух максимальных чисел равна {numbers_sum}')
