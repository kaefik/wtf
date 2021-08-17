"""
 сущность Отзывы

"""
from datetime import datetime
from typing import Optional, List, Dict, Any

from addtypes import Rating
from toilet import Toilet


# Отзывы
class Comment:

    def __init__(self):
        # уникальный номер
        self._id: Optional[int] = None  # ? здесь скорее всего нужна генерация уникального номера
        # Активный отзыв
        self._active: bool = False
        # туалет к которому отзыв
        self._toilet: Optional[Toilet] = None
        # автор
        self._author: str = "guest"
        # текст отзыва
        self._text: str = ""
        # массив фотографий ??
        self._photo: List[str] = []
        self._rating: Rating = Rating.no
        # дата публикации
        self._date: datetime = datetime(2021, 1, 1)
        # статус публикации, если False - черновик
        self._published: bool = False

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, my_id: int) -> None:
        self._id = my_id

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, status: bool) -> None:
        self._active = status

    @property
    def toilet(self) -> Optional[Toilet]:
        return self._toilet

    @toilet.setter
    def toilet(self, new_toilet: Optional[Toilet]) -> None:
        self._toilet = new_toilet

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        self._author = new_author

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    @property
    def photo(self) -> List[str]:
        return self._photo

    @photo.setter
    def photo(self, new_photo: List[str]) -> None:
        self._photo = new_photo

    @property
    def rating(self) -> Rating:
        return self._rating

    @rating.setter
    def rating(self, new_rating: Rating) -> None:
        self._rating = new_rating

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

    def to_json(self) -> Dict[str, Any]:
        """
        преобразование в словарь
        :return:
        """
        result = dict()
        result["id"] = self.id
        result["active"] = self.active
        result["toilet"] = self.toilet
        result["author"] = self.author
        result["text"] = self.text
        result["photo"] = self.photo
        result["rating"] = self.rating
        result["date"] = self.date
        result["published"] = self.published


if __name__ == "__main__":
    obj = Comment()
    obj.id = 10
    print(obj.to_json())
