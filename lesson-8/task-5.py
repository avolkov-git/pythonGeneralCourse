# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.

import task_4
from random import randint


def admission(warehouse, equipment):
    warehouse._add_equipment_(equipment)


def division_transfer():
    pass


general_warehouse = task_4.Warehouse('Нижний Новгород')

for index in range(10):
    printer = task_4.Printer(f'Printer {index}', 'Intel LLC.', randint(100, 200))
    admission(general_warehouse, printer)

print(general_warehouse.equipment_items, general_warehouse.equipment_count)
