# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(ZeroDivisionError):

    def __init__(self):
        self.text = 'На ноль делить нельзя, выберите другое число'


user_num = int(input('Введите число, на которое хотели бы разделить число 100: '))
try:
    if user_num == 0:
        raise MyZeroDivisionError
    else:
        result = 100 / user_num
    print(result)
except MyZeroDivisionError as div_err:
    print(div_err.text)

print('Завершение скрипта')
