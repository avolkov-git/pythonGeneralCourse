# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('task-5.txt', 'r+', encoding='utf-8') as txt_file:
    random_nums = [randint(0, 100) for index in range(20)]
    print(random_nums)

    # Записываем набор random_nums в файл txt_for_write
    print(*random_nums, file=txt_file, sep=' ')

    # Перемещаемся в начало файла
    txt_file.seek(0)

    line = txt_file.readline()
    splt_line = line.split()

    numbers_sum = 0
    for number in splt_line:
        numbers_sum += int(number)

    print(f'Сумма чисел в файле: {numbers_sum}')
