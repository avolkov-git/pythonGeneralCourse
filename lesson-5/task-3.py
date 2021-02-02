# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

with open('task-3.txt', 'r', encoding='utf-8') as txt_file:
    # Определение сотрудников с зарплатой менее 20 000
    salary_less_20k = []
    # Переменная для подсчета средней заработной платы
    salary_sum = 0
    lines_count = len(txt_file.readlines())
    txt_file.seek(0)

    for txt_line in map(lambda line: line.rstrip('\n'), txt_file):
        spl_line = txt_line.split(',')
        salary_sum += int(spl_line[1])

        if int(spl_line[1]) < 20000:
            salary_less_20k.append(spl_line[0])

    print(f'Сотрудники с окладом менее 20000: {salary_less_20k}')

    salary_avg = salary_sum / lines_count
    print(f'Средняя зарплата сотрудников: {salary_avg}')
