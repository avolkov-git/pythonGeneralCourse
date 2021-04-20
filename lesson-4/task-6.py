# 6. Реализовать два небольших скрипта:
#   а) итератор, генерирующий целые числа, начиная с указанного,
#   б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

start_number = None

while start_number is None:
    try:
        start_number = int(input('Введите начальное число: '))
    except ValueError:
        print('Вы ввели не число')

# а) итератор, генерирующий целые числа, начиная с указанного,
for number in count(start_number):
    print(number)
    # Останавливаем цикл
    if number == 10:
        break

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
breaker = 0

new_list = ['A', 'B', 'C']
for element in cycle(new_list):
    print(element)

    breaker += 1
    if breaker > 30:
        break