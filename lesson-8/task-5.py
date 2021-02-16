# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.

from task_4 import Printer, Scanner, Xerox, Warehouse, Division
from random import randint


def admission(warehouse, equipment):
    warehouse.add_item(equipment)


def division_transfer(warehouse, division, equipment):
    warehouse.item_transfer(division, equipment)


general_warehouse = Warehouse('Нижний Новгород')
adm_division = Division('Администрация')

for index in range(10):
    printer = Printer(f'Printer {index}', 'Intel LLC.', randint(100, 200))
    admission(general_warehouse, printer)

for index in range(5):
    scanner = Scanner(f'Scanner {index}', 'Intel LLC.', randint(100, 200))
    admission(general_warehouse, scanner)

for index in range(8):
    xerox = Xerox(f'Xerox {index}', 'Intel LLC.', randint(100, 200))
    admission(general_warehouse, xerox)

print(f'Остатки на складе {general_warehouse}: {general_warehouse.equipment_count}')
# general_warehouse.print_items_list()
print(f'Перемещаем {xerox} в подразделение {adm_division}')
division_transfer(general_warehouse, adm_division, xerox)
print(f'Остатки на подразделении {adm_division}: {adm_division.equipment_count}')
print(f'Остатки на складе {general_warehouse}: {general_warehouse.equipment_count}')


