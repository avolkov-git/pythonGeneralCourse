# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.
def devide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 0
    else:
        return None


while True:
    numerator = None
    while numerator is None:
        try:
            numerator = int(input('Введите числитель: '))
        except ValueError:
            print('Числитель должен быть числом!')

    denominator = None
    while denominator is None:
        try:
            denominator = int(input('Введите знаменатель: '))
        except ValueError:
            print('Знаменатель должен быть числом!')

    result = devide_numbers(numerator, denominator)

    if result == 0:
        print('Знаменатель равен нулю. Деление невозможно!')
    elif result is None:
        print('При делении возникла ошибка. Попробуйте еще раз')
    else:
        print(f'{numerator} / {denominator} = {result}')
        break
