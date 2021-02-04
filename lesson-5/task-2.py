# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

# Способ 1. Подсчет через чтение всех строк файла
with open('task-2.txt', 'r') as txt_file:
    file_content = txt_file.readlines()
    for line in file_content:
        print(f'{len(line.split())} слов в строке')
    print(f'Количество строк в текстовом файле: {len(file_content)}')

# Способ 2. Чтение всего файла
counter = 0

with open('task-2.txt', 'r') as txt_file:
    for index in file_content:
        print(f'{len(index.split())} слов в строке')
        counter += 1

    print(f'Количество строк в текстовом файле: {counter}')

# Способ 3. Чтение файла построчно
line_txt = None

with open('task-2.txt', 'r') as txt_file:
    counter = -1  # Отсекаем условие line_txt = None

    while line_txt or line_txt is None:
        line_txt = txt_file.readline()
        print(f'{len(line_txt.split())} слов в строке')
        counter += 1

    print(f'Количество строк в текстовом файле: {counter}')
