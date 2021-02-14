# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

from random import randint


class Matrix:
    def __init__(self, matrix, matrix_name, matrix_width, matrix_height):
        self.__matrix_data__ = matrix
        self.__matrix_name__ = matrix_name
        self.__matrix_width__ = matrix_width
        self.__matrix_height__ = matrix_height

    def __str__(self):
        matrix_view = f'{self.__matrix_name__}: ' + '\n'

        for index in range(self.__matrix_height__):
            this_level = self.__matrix_data__[index]
            matrix_view += f'{this_level}' + '\n'

        return matrix_view

    def __add__(self, other):
        list_result = self.create_matrix_list(self.__matrix_width__, self.__matrix_height__, True)
        for index in range(self.__matrix_height__):
            list_result[index] = self.__list_sum__(list_result[index], self.__matrix_data__[index])
            list_result[index] = self.__list_sum__(list_result[index], other.__matrix_data__[index])

        result_matrix = Matrix(list_result, 'Матрица результат сложения', self.__matrix_width__,
                               self.__matrix_height__)

        return result_matrix

    @staticmethod
    def __list_sum__(a_list, b_list):
        return [x + y for x, y in zip(a_list, b_list)]

    @staticmethod
    def create_matrix_list(width, height, empty_matrix=False):
        max_value = 0 if empty_matrix else 100
        result = [[randint(0, max_value) for element in range(width)] for index in range(height)]

        return result


def input_matrix_param(param_name):
    while matrix_size := input(f'Введите {param_name} матрицы: '):
        try:
            matrix_size = int(matrix_size)
            break
        except ValueError:
            print('Значение должно быть указано числом!')

    return matrix_size


matrix_width = input_matrix_param('ширину')
matrix_height = input_matrix_param('высоту')

a_matrix = Matrix.create_matrix_list(matrix_width, matrix_height)
b_matrix = Matrix.create_matrix_list(matrix_width, matrix_height)

a_matrix_obj = Matrix(a_matrix, 'Матрица A', matrix_width, matrix_height)
b_matrix_obj = Matrix(b_matrix, 'Матрица B', matrix_width, matrix_height)

print(a_matrix_obj)
print(b_matrix_obj)

print(a_matrix_obj + b_matrix_obj)
