# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.
usr_string = None

with open('task-1.txt', 'w') as txt_file:
    while usr_string or usr_string is None:
        usr_string = input('Введите текстовое сообщение (для выхода введите пустое сообщение): ')
        if usr_string:
            print(usr_string, file=txt_file)
