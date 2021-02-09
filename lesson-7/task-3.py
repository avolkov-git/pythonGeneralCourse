# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n*****. Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class OrganicCell:
    count_of_cells: int = 0

    def __add__(self, other):
        __new_cell = OrganicCell()
        __new_cell.count_of_cells = self.count_of_cells + other.count_of_cells
        return __new_cell

    def __sub__(self, other):
        __new_cell = OrganicCell()
        __new_cell.count_of_cells = self.count_of_cells - other.count_of_cells
        return __new_cell if __new_cell.count_of_cells > 0 else None

    def __mul__(self, other):
        __new_cell = OrganicCell()
        __new_cell.count_of_cells = self.count_of_cells * other.count_of_cells
        return __new_cell

    def __truediv__(self, other):
        try:
            __new_cell = OrganicCell()
            __new_cell.count_of_cells = int(self.count_of_cells / other.count_of_cells)
            return __new_cell
        except ValueError:
            return None

    def __str__(self):
        return f'Клетка, содержащая {self.count_of_cells} ячейки'

    def make_order(self, row):
        last_cells = self.count_of_cells % row
        rows_count = int(self.count_of_cells / row)
        return 'Ячейки по рядам ({} в ряд): \n'.format(row) + ((('*' * row)+'\n') * rows_count) + ('*' * last_cells)


first_cell = OrganicCell()
first_cell.count_of_cells = 15
print('_' * 30)
print(first_cell)
print(first_cell.make_order(4))

second_cell = OrganicCell()
second_cell.count_of_cells = 49
print('_' * 30)
print(second_cell)
print(second_cell.make_order(10))

add_cell = first_cell + second_cell
print('_' * 30)
print('Результат сложения клеток: ')
print(add_cell)
print(add_cell.make_order(12))

sub_cell = first_cell - second_cell
if sub_cell:
    print('_' * 30)
    print('Результат вычитания клеток: ')
    print(sub_cell)
    print(sub_cell.make_order(6))
else:
    print('_' * 30)
    print('Результат вычитания клеток: ')
    print('В результате вычитания двух клеток появилась клетка, количество ячеек которой меньше нуля')

mul_cell = first_cell * second_cell
print('_' * 30)
print('Результат умножения клеток: ')
print(mul_cell)
print(mul_cell.make_order(90))

truediv_cell = first_cell / second_cell
if truediv_cell:
    print('_' * 30)
    print('Результат деления клеток: ')
    print(truediv_cell)
    print(truediv_cell.make_order(5))
else:
    print('_' * 30)
    print('Результат деления клеток: ')
    print('Вторая клетка не содержит ячейки. Деление на 0 невозможно')
