# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Warehouse:
    pass


class OfficeEquipment:
    voltage = 220
    # Сквозная нумерация серийных номеров
    global_serial_num = 1

    def __init__(self, name, manufacturer, serial_prefix=''):
        self.name = name
        self.manufacturer = manufacturer
        self.serial_num = serial_prefix + str(OfficeEquipment.global_serial_num)

        OfficeEquipment.global_serial_num += 1


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


printer = Printer('Print', 'Xerox', 500)
scanner = Scanner('Scanner', 'Xerox', True)
xerox = Xerox('Xerox', 'Xerox', 50)
