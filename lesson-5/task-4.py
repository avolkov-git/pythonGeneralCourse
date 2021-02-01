# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

number_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

read_file = open('task-4.txt', 'r', encoding='utf-8')
# Файл будет создан при его отсутствии, поэтому можно считать, что условие "Новый блок строк должен записываться в
# новый текстовый файл" выполнено.
write_file = open('task-4-result.txt', 'w', encoding='utf-8')

# Но если нет, то можно раскомментировать этот код, вместо того, что выше, в таком случае файл будет создаваться каждый
# раз новый
# from os.path import exists
# import tempfile


# write_file_name = 'task-4-result.txt'
# if exists('task-4-result.txt'):
#     write_file_name = next(tempfile._get_candidate_names()) + '.txt'

# write_file = open(write_file_name, 'w', encoding='utf-8')


for read_line in read_file:
    # Читаем значения строки
    splt_read_line = read_line.split(' - ')

    # Делим строку на два значения (ключ, значение) формата DISCRIP - NUM
    write_key = number_dict[splt_read_line[0]]
    write_value = splt_read_line[1].rstrip('\n')

    # Записываем пару в файл
    write_file.write(f'{write_key} - {write_value} \n')

read_file.close()
write_file.close()
