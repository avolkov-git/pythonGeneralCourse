income = int(input('Введите значение выручки (руб.): '))
expenses = int(input('Введите значение затрат (руб.): '))

result = income - expenses

if result < 0:
    print('Убыток составил {} руб.'.format(result*(-1)))
else:
    print('Выручка составила {} руб.'.format(result))
    rent = round(result / income, 3) * 100
    print('Рентабельность составила {}%'.format(rent))

    employeesCount = int(input('Укажите количество сотрудников: '))
    print('На каждого сотрудника приходится {} руб.'.format(result/employeesCount))
