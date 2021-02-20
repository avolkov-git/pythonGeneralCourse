# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class ListError(ValueError):
    def __init__(self):
        self.text = 'Список может содержать только числа!'


my_list = []
while True:
    try:
        usr_value = input("Введите число в список (или введите 'stop' для выхода): ")
        if usr_value == 'stop':
            break
        if not usr_value.isdigit():
            raise ListError()
        my_list.append(int(usr_value))
    except ListError as ex:
        print(ex.text)

print(my_list)
