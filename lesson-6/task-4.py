# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.

from random import randint

class Car:
    speed = 0

    def __init__(self, name, color, is_police: bool = False):
        self.name = name
        self.color = color
        self.is_police = is_police

    def __speeding_report__(self):
        print(f'{self.name} сбавьте скорость!')

    @staticmethod
    def go():
        print('Машина завелась. Начинаем движение...')

    @staticmethod
    def stop():
        print('Машина остановилась. Глушим двигатель...')

    def turn(self, direction):
        print(f'Машина повернула {direction}')
        # На поворотах принято сбрасывать, чтобы не вылететь :)
        if self.speed >= 60:
            self.speed_down(10)

    def speed_up(self, speed_up_value):
        self.speed += speed_up_value
        print('Едем прямо, набираем скорость')
        self.show_speed(False)

    def speed_down(self, speed_down_value):
        self.speed -= speed_down_value

    def show_speed(self, hide_show=False):
        if not hide_show:
            print(f'Текущая скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self, hide_show=False):
        super(TownCar, self).show_speed(hide_show)
        if self.speed > 60:
            self.__speeding_report__()
            self.speed_down(10)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, hide_show=False):
        super(WorkCar, self).show_speed(hide_show)
        if self.speed > 40:
            self.__speeding_report__()
            self.speed_down(10)


class PoliceCar(Car):

    def __init__(self, name, color):
        super().__init__(self, name, color)
        self.is_police = True


new_town_car = TownCar('Renault Logan', 'blue')
new_work_car = WorkCar('Ford Transit', 'white')
new_police_car = PoliceCar('Ford Explorer', 'white')

new_town_car.go()
new_town_car.speed_up(20)
new_town_car.show_speed()
# Пытаемся "покатать" машину рандомно
# В range указываем количество выполняемых действий (итераций)
for index in range(randint(10, 25)):
    # Логика простая, если выпадает 0, значит прибавляем скорость (движемся прямо), если 1, то едем налево, 2 - направо
    action = randint(0, 2)
    if action == 1:
        new_town_car.speed_up(10)
    elif action == 0:
        new_town_car.turn('налево')
    elif action == 2:
        new_town_car.turn('направо')

new_work_car.stop()
