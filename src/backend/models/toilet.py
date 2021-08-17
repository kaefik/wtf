"""
сущность Туалет

* внешние координаты расположения здания в котором находится туалет (географические координаты на карте)
* внутреннее расположение туалета внутри здания (все здание или точное расположение туалета - этаж и т д. )
* доступность туалета (свободный вход или нет)
* платность туалета (платный, бесплатный)
* вода в кране для рук (нет воды, только холодная, есть горячая)
* мыло для рук (есть/нет)
* сушилка для рук (есть/нет)
* туалетная бумага (отдельный аппарат, в каждой кабинке есть или нет)
* унитаз (писсуар) для детей
* количество кабинок
"""

from datetime import datetime
from typing import Optional, Dict, Any

from addtypes import Sex, Water, GeoCoords


#  Туалет
class Toilet:

    def __init__(self):
        # уникальный номер
        self._id: Optional[int] = None  # ? здесь скорее всего нужна генерация уникального номера
        self._title: str = ""
        # географические координаты - адрес
        self._loc = GeoCoords()  # TODO: проработать географические координаты
        # долготу и широту, latitude, longitude
        # внутреннее расположение в здании (описание)
        self._placement: str = ""
        # стоимость посещения
        self._price: float = 0.0
        # вода
        self._water: Water = Water.no
        # мыло
        self._soap: bool = False
        # туалетная бумага
        self._paper: bool = False
        # сушка для рук
        self._dryer: bool = False
        # неприятный запах
        self._smell: bool = False
        # унитаз для детей
        self._child_toilet: bool = False
        # кол-во кабинок
        self._cabin: int = 0
        # тип туалета ??
        self._type_toilet: Sex = Sex.man
        # время создания объекта
        self._date: datetime = datetime(2021, 1, 1)
        # статус опубликования туалета
        self._published: bool = False
        # фотографии
        # основная фотография
        self._photo_main: str = ""  # ссылка на фотографии
        # активный объект или нет
        self._active: bool = False

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, my_id: int) -> None:
        self._id = my_id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @property
    def location(self) -> GeoCoords:
        return self._loc

    @location.setter
    def location(self, loc: GeoCoords) -> None:
        # TODO: проработать географические координаты
        self._loc = loc

    @property
    def placement(self) -> str:
        return self._placement

    @placement.setter
    def placement(self, place: str) -> None:
        self._placement = place

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        self._price = new_price

    @property
    def water(self) -> Water:
        return self._water

    @water.setter
    def water(self, status_water: Water) -> None:
        self._water = status_water

    @property
    def soap(self) -> bool:
        return self._soap

    @soap.setter
    def soap(self, status: bool) -> None:
        self._soap = status

    @property
    def paper(self) -> bool:
        return self._paper

    @paper.setter
    def paper(self, status: bool) -> None:
        self._paper = status

    @property
    def dryer(self) -> bool:
        return self._dryer

    @dryer.setter
    def dryer(self, status: bool) -> None:
        self._dryer = status

    @property
    def smell(self) -> bool:
        return self._smell

    @smell.setter
    def smell(self, status: bool) -> None:
        self._smell = status

    @property
    def child(self) -> bool:
        return self._child_toilet

    @child.setter
    def child(self, status: bool) -> None:
        self._child_toilet = status

    @property
    def count_cabin(self) -> int:
        return self._cabin

    @count_cabin.setter
    def count_cabin(self, count: int) -> None:
        self._cabin = count

    @property
    def sex(self) -> Sex:
        return self._type_toilet

    @sex.setter
    def sex(self, new_sex: Sex) -> None:
        self._type_toilet = new_sex

    @property
    def date(self) -> datetime:
        return self._date

    @date.setter
    def date(self, new_date: datetime) -> None:
        self._date = new_date

    @property
    def published(self) -> bool:
        return self._published

    @published.setter
    def published(self, status: bool) -> None:
        self._published = status

    @property
    def photo(self) -> str:
        return self._photo_main

    @photo.setter
    def photo(self, new_photo: str) -> None:
        self._photo_main = new_photo

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, status: bool) -> None:
        self._active = status

    def to_json(self) -> Dict[str, Any]:
        """
        преобразование в словарь
        :return:
        """
        result = dict()
        result["id"] = self.id
        result["title"] = self.title
        result["location"] = self.location
        result["placement"] = self.placement
        result["price"] = self.price
        result["water"] = self.water
        result["soap"] = self.soap
        result["paper"] = self.paper
        result["dryer"] = self.dryer
        result["smell"] = self.smell
        result["child"] = self.child
        result["cabin"] = self.count_cabin
        result["sex"] = self.sex
        result["date"] = self.date
        result["published"] = self.published
        result["photo_main"] = self.photo
        result["active"] = self.active
        return result


if __name__ == "__main__":
    obj = Toilet()
    obj.id = 10
    print(obj.to_json())
