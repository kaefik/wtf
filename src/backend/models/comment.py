"""
 сущность Отзывы

"""
from datetime import datetime.datetime
from typing import Optional

from addtypes import Rating
from toilet import Toilet


# Отзывы
class Comment:

    def __init__(self):
        # уникальный номер
        self.id: Optional[int] = None  # ? здесь скорее всего нужна генерация уникального номера
        # Активный отзыв
        self.is_active: bool = False
        # туалет к которому отзыв
        self.toilet: Toilet = None
        # автор
        self.author: str = "guest"
        # текст отзыва
        self.text: str = ""
        # массив фотографий ??
        self.photo = []
        self.rating: Rating = Rating.no
        # дата публикации
        self.date: datetime = datetime(2021, 01, 01)
        # статус публикации, если False - черновик
        self.published: bool = False
