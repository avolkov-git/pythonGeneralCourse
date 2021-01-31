# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать
# генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint
from mylib import max_numbers_list

number_list = [randint(0, 100) for index in range(10)]
print(number_list)

max_numbers_generator = max_numbers_list(number_list)

result_list = []
for max_number in max_numbers_generator:
    result_list.append(max_number)

print(result_list)
