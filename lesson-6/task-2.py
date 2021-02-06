# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу
# метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    __weight = 25
    __height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculate(self, ):
        return int(self._length * self._width * self.__weight * self.__height / 1000)


length = None
while not length:
    try:
        length = int(input('Введите протяженность дорожного полотна: '))
    except ValueError:
        print('Вы ввели не число!')
        length = None

width = None
while not width:
    try:
        width = int(input('Введите ширину дорожного полотна: '))
    except ValueError:
        print('Вы ввели не число!')
        width = None

new_road = Road(length, width)
print(f'Масса дороги протяженностью {length}м. и шириной {width}м. составит {new_road.mass_calculate()}т.')
