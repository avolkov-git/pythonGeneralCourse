# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
# обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) 10(лаб)
# Физкультура: 30(пр)
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re


# Удаляем все, кроме цифр
def form_number(string):
    re.compile('\D+')
    return re.sub('\D+', '', string)


# Удаляем все, кроме строк и цифр
def form_string(string):
    re.compile('\W+')
    return re.sub('\W+', '', string)


result_dict = {}

with open('task-6.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.readlines()

    for subject_data in txt_content:
        sum_of_hours = 0
        subject_name = ''
        # Разбиваем строку на элементы для подсчета
        splt_data = subject_data.split()
        for data_element in splt_data:
            format_number = form_number(data_element)
            # Если после удаления всего, кроме цифр строка не осталась пустой, значит строка содержит количество часов
            if format_number != '':
                result_dict[subject_name] += int(format_number)
            # Иначе это название предмета
            else:
                subject_name = form_string(data_element)
                result_dict[subject_name] = 0

    print(result_dict)
