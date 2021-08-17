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


class GeoCoords:
    """
    класс для хранения географических координат
    """

    def __init__(self, lat: float = 0.0, long: float = 0.0) -> None:
        self._latitude: float = 0.0  # долгота
        self._longitude: float = 0.0  # широта

    @property
    def lat(self) -> float:
        return self._latitude

    @lat.setter
    def lat(self, new_lat: float) -> None:
        self._latitude = new_lat

    @property
    def long(self) -> float:
        return self._longitude

    @long.setter
    def long(self, new_long: float) -> None:
        self._longitude = new_long
