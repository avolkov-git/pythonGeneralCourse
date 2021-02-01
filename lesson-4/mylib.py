from math import factorial


# Для задания №1 (Функция расчета заработной платы)
def payroll_calculation(hours, rate):
    try:
        return int(hours) * int(rate)
    except ValueError:
        print('Incorrect hours or rate value')
        return 0


# Для задания №2 (Функция генератора проверки числа. Проверка что текущее больше предыдущего)
def max_numbers_list(number_list):
    prev = None
    for number in number_list:
        if prev is not None:
            if number > prev:
                prev = number
                yield number
        prev = number


# Для задания №5 (Функция для reduce)
def sum_of_two(rev_element, element):
    return rev_element + element


# Для задания №7 (Функция генератора факториала)
def fact(n):
    iterator = 1

    for index in range(1, n + 1):
        # Конструкцию *= подсмотрел на стак оверфлоу
        iterator *= index
        yield iterator


# Для задания №7 (Функция генератора факториала с использованием библиотеки math)
def math_fact(n):
    for index in range(1, n + 1):
        yield factorial(index)
