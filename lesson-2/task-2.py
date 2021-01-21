"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input().
"""
input_list = []

while True:
    if len(input_list) > 2:
        break

    input_text = input('Введите значения через ПРОБЕЛ для добавления их в список (несколько значений в одной строке): ')
    user_list = input_text.split(' ')
    # На всякий случай удалим пробелы, которые являются элементами списка (в случае, если случайно несколько раз его
    # нажали при вводе)
    try:
        while True:
            user_list.remove('')
    except ValueError:
        errMsg = 'Эта строка для того, чтобы не обрабатывать исключение'

    if len(user_list) < 2:
        input_list.extend(user_list)
        print('Вы ввели слишком мало значений. Пожалуйста, укажите больше (новые значения будут добавлены к уже '
              'введенным')
    else:
        input_list.extend(user_list)
        break

print(f'Ваш список: {input_list}')

# Вариант решения с циклом for для последовательностей с обработкой исключения
test_list = input_list.copy()
skip = False
for index, this_value in enumerate(test_list):
    if not skip:
        try:
            next_value = test_list[index + 1]
            test_list[index + 1] = this_value
            test_list[index] = next_value
            skip = True
        except IndexError:
            break

    else:
        skip = False
print(test_list)

# Вариант решения с циклом for для последовательностей с расчетом чётности числа
test_list = input_list.copy()
for index, this_value in enumerate(test_list):
    if index == 0 or ((index % 2 == 0) and index + 1 < len(test_list)):
        next_value = test_list[index + 1]
        test_list[index + 1] = this_value
        test_list[index] = next_value
    else:
        continue
print(test_list)

# Вариант решения с циклом while
test_list = input_list.copy()
index_counter = 1
while True:
    if index_counter < len(test_list):
        this_value = test_list[index_counter]
        pre_value = test_list[index_counter - 1]
        test_list[index_counter] = pre_value
        test_list[index_counter - 1] = this_value
        index_counter += 2
    else:
        break
print(test_list)

# Вариант решения с циклом for для диапазона
test_list = input_list.copy()
for list_element in range(0, len(test_list) - 1):
    if list_element == 0 or list_element % 2 == 0:
        this_value = test_list[list_element]
        next_value = test_list[list_element + 1]
        test_list[list_element] = next_value
        test_list[list_element + 1] = this_value
    else:
        continue
print(test_list)
