# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class DayFormatError(ValueError):
    text = 'Дата выходит за границу 1 - 31'


class MonthFormatError(ValueError):
    text = 'Месяц выходит за границу 1-12'


class YearFormatError(ValueError):
    text = 'Неправильный формат года. Ожидается: YYYY'


class Date:

    @classmethod
    def date_to_int(cls, str_date):
        date_array = str_date.split('-')
        result = []
        try:
            for value in date_array:
                result.append(int(value))
        except ValueError:
            print('Все параметры даты должны быть числовыми значениями!')

        return result

    @staticmethod
    def date_validation(date_data):
        dd = date_data[0]
        mm = date_data[1]
        yy = date_data[2]

        if 0 < dd <= 31:
            pass
        else:
            raise DayFormatError(DayFormatError.text)

        if 0 < mm <= 12:
            pass
        else:
            raise MonthFormatError(MonthFormatError.text)

        if len(str(yy)) == 4:
            pass
        else:
            raise YearFormatError(YearFormatError.text)

    def __init__(self, str_date):

        date_data = Date.date_to_int(str_date)
        Date.date_validation(date_data)

        self.dd = f'{date_data[0]:02}'
        self.mm = f'{date_data[1]:02}'
        self.yy = f'{date_data[2]:04}'


user_date = input('Введите дату формата DD-MM-YYYY: ')
date_obj = Date(user_date)

print(date_obj.dd, date_obj.mm, date_obj.yy)
