# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.

from task_4 import Printer, Scanner, Xerox, Warehouse
from random import randint


def admission(warehouse, equipment):
    warehouse.add_item(equipment)


def division_transfer():
    pass


general_warehouse = Warehouse('Нижний Новгород')

for index in range(10):
    printer = Printer(f'Printer {index}', 'Intel LLC.', randint(100, 200))
    admission(general_warehouse, printer)

for index in range(5):
    scanner = Scanner(f'Scanner {index}', 'Intel LLC.', randint(100, 200))
    admission(general_warehouse, scanner)

for index in range(8):
    xerox = Xerox(f'Xerox {index}', 'Intel LLC.', randint(100, 200))
    admission(general_warehouse, xerox)

print(general_warehouse.equipment_count)
