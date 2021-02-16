# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, address):
        self.address = address
        self.equipment_items = []
        self.equipment_count = {'printers': 0, 'scanners': 0, 'xerox': 0}

    def __str__(self):
        return f'Склад {self.address}'

    @classmethod
    def add_items_to_results(cls, obj, equipment):
        if type(equipment) == Printer:
            obj.equipment_count['printers'] += 1
        elif type(equipment) == Scanner:
            obj.equipment_count['scanners'] += 1
        elif type(equipment) == Xerox:
            obj.equipment_count['xerox'] += 1

    def add_item(self, equipment):
        self.equipment_items.append(equipment)
        Warehouse.add_items_to_results(self, equipment)

    def item_transfer(self, division, equipment):
        try:
            # Удаляем оборудование со склада
            self.equipment_items.remove(equipment)
            if type(equipment) == Printer:
                self.equipment_count['printers'] -= 1
            elif type(equipment) == Scanner:
                self.equipment_count['scanners'] -= 1
            elif type(equipment) == Xerox:
                self.equipment_count['xerox'] -= 1

            # Перемещаем оборудование в подразделение
            division.equipment_items.append(equipment)
            Warehouse.add_items_to_results(division, equipment)
        except ValueError:
            print(f'Оборудование {equipment} не найдено на складе {self}')

    def print_items_list(self):
        for item in self.equipment_items:
            print(item)


class Division:
    def __init__(self, name):
        self.name = name
        self.equipment_items = []
        self.equipment_count = {'printers': 0, 'scanners': 0, 'xerox': 0}

    def __str__(self):
        return self.name

    def print_items_list(self):
        for item in self.equipment_items:
            print(item)


class OfficeEquipment:
    voltage = 220
    # Сквозная нумерация серийных номеров
    global_serial_num = 1

    def __init__(self, name, manufacturer, serial_prefix=''):
        self.name = name
        self.manufacturer = manufacturer
        self.serial_num = f'{serial_prefix}-{OfficeEquipment.global_serial_num}'

        OfficeEquipment.global_serial_num += 1

    def __str__(self):
        return f'{self.name} ({self.serial_num})'


class Printer(OfficeEquipment):

    def __init__(self, name, manufacturer, max_paper_piece: int):
        self.max_paper_piece = max_paper_piece
        super().__init__(name, manufacturer, 'P')


class Scanner(OfficeEquipment):
    def __init__(self, name, manufacturer, streaming: bool):
        self.streaming = streaming
        super().__init__(name, manufacturer, 'S')


class Xerox(OfficeEquipment):
    def __init__(self, name, manufacturer, max_copy: int):
        self.max_copy = max_copy
        super().__init__(name, manufacturer, 'X')
