# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
# за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from mylib import fact
from mylib import math_fact

factorial_number = None

while factorial_number is None:
    try:
        factorial_number = int(input('Введите число для расчета факториала: '))
    except ValueError:
        print('Вы ввели не число')

# Используя собственную функцию расчета факториала
for element in fact(factorial_number):
    print(element)

print('-----------------')

# Используя функцию factorial из библиотеки math
for element in math_fact(factorial_number):
    print(element)
