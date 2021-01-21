"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а
указать явно, в программе.
"""


# Скрипт проверки типов данных
def type_check(value, expect_value):
    check_result = type(value) == expect_value
    print(f'Результат проверки значения {value} на тип {expect_value}: {check_result}')


# Простые и примитивные типы

new_int = 10
type_check(new_int, int)
new_float = 10.3
type_check(new_float, float)
new_complex = complex(5, 6)
type_check(new_complex, complex)
new_string = '10.3'
type_check(new_string, str)
new_bool = True
type_check(new_bool, bool)
new_none = None
type_check(new_none, None)
new_bytes = bytes('Some string'.encode("utf-8"))
type_check(new_bytes, bytes)

# Списки и прочее
new_list = [new_int, new_float, new_complex, new_string, new_bool, new_none, new_bytes]
type_check(new_list, list)
new_tuple = (new_int, new_float, new_complex, new_string, new_bool, new_none, new_bytes)
type_check(new_tuple, tuple)
new_set = {new_int, new_float, new_complex, new_string, new_bool, new_none, new_bytes}
type_check(new_set, set)
new_dict = {'key_1': new_int, 'key_2': new_tuple, 'key_3': new_complex, 'key_4': new_string, 'key_5': new_bool,
            'key_6': new_none, 'key_7': new_bytes}
type_check(new_dict, dict)

# Исключение
try:
    new_err_1 = 100 / 0
except Exception as err_msg:
    new_err_1 = err_msg

try:
    new_err_2 = 'Some text' + 1
except Exception as err_msg:
    new_err_2 = err_msg

try:
    new_err_3 = new_tuple.pop()
except Exception as err_msg:
    new_err_3 = err_msg

try:
    new_err_4 = bytes('Some string')
except Exception as err_msg:
    new_err_4 = err_msg

try:
    new_err_5 = someText
except Exception as err_msg:
    new_err_5 = err_msg

try:
    new_err_6 = new_list[999]
except Exception as err_msg:
    new_err_6 = err_msg

try:
    new_err_7 = new_dict['key_8']
except Exception as err_msg:
    new_err_7 = err_msg

result_list = [new_int, new_float, new_complex, new_string, new_bool, new_none, new_bytes, new_list, new_tuple, new_set,
               new_dict, new_err_1, new_err_2, new_err_3, new_err_4, new_err_5, new_err_6, new_err_7]

for list_value in result_list:
    print(type(list_value))
