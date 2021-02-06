# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __colors = [
        {'color': 'Красный', 'timeout': 7, 'next_color_index': 1},
        {'color': 'Желтый', 'timeout': 2, 'next_color_index': 2},
        {'color': 'Зеленый', 'timeout': 5, 'next_color_index': 0},
    ]
    __color = 0

    def running(self, __iterations_number):
        print('Включаем светофор...')
        self.__switch_color(self.__color, __iterations_number)

    def __shutdown_light(self):
        print('Выключаем светофор...')
        exit(0)

    def __switch_color(self, color_index, __iterations_number):

        for index in range(__iterations_number):
            print(f"Текущий цвет: {self.__colors[color_index].get('color')}")
            sleep(self.__colors[color_index].get('timeout'))
            color_index = self.__colors[color_index].get('next_color_index')

        self.__shutdown_light()


iterations_number = None
while not iterations_number:
    iterations_number = input('Введите количество итераций переключения светофора (числом): ')
    try:
        iterations_number = int(iterations_number)
    except ValueError:
        iterations_number = None
        print('Вы ввели не число')

new_traffic_light = TrafficLight()
new_traffic_light.running(iterations_number)
