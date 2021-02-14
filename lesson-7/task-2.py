# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def consumption_calculating(self):
        pass

    @abstractmethod
    def clothes_view(self):
        pass


class Coat(Clothes):
    def consumption_calculating(self):
        return round(self.size / 6.5 + 0.5, 2)

    @property
    def clothes_view(self):
        return f'{self.name}, размер: {self.size}'


class Suit(Clothes):
    def consumption_calculating(self):
        return round(2 * self.size + 0.3, 2)

    @property
    def clothes_view(self):
        return f'{self.name}, рост: {self.size}'


new_coat = Coat('Пальто мужское', 48)
new_suit = Suit('Костюм тройка', 177)

print(f'Для пошива {new_coat.clothes_view} потребуется {new_coat.consumption_calculating():.2f}м. ткани')
print(f'Для пошива {new_suit.clothes_view} потребуется {new_suit.consumption_calculating():.2f}м. ткани')
