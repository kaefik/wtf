"""
вспомогательный модуль для определения необходимых типов
"""

from enum import Enum


# тип Вода
class Water(Enum):
    no = 0  # Нет воды
    cold = 1  # холодная вод
    hot = 2  # горячая вода
    warm = 3  # теплая вода


# тип туалета
class Sex(Enum):
    man = 1  # мужской
    women = 2  # женский
    nomobile = 3  # немобильные
    mother = 4  # мать и детя


# тип Рейтинга
class Rating(Enum):
    no = 0
    very_bad = 1
    bad = 2
    soso = 3
    good = 4
    recommend = 5
