"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

usr_string = input('Введите несколько строк разделенных пробелами: ')
split_string = usr_string.split(' ')

# С использованием enumerate
for str_number, split_element in enumerate(split_string):
    printing_string = split_element
    if len(printing_string) > 10:
        printing_string = printing_string[:10]

    print(str_number + 1, printing_string)



