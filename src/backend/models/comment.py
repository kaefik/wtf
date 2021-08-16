"""
 сущность Отзывы

"""


# Отзывы
class Comment:
    pass
    # RATING_CHOICES = [
    #     (0, 'Без оценки'),
    #     (1, 'Очень плохо'),
    #     (2, 'Плохо'),
    #     (3, 'Удовлетворительно'),
    #     (4, 'Хорошо'),
    #     (5, 'Рекомендую'),
    # ]
    #
    # is_active = models.BooleanField(default=True, verbose_name='Активный отзыв')
    # # туалет к которому отзыв
    # toilet = models.ForeignKey(Toilet, null=False, on_delete=models.PROTECT,
    #                            verbose_name='Туалет')
    # author = models.CharField(default="guest" ,max_length=30, verbose_name='Автор')
    # text = models.TextField(verbose_name='Текст отзыва')
    # # массив фотографий ??
    # # photo = models.ImageField()
    # rating = models.IntegerField(default=0, choices=RATING_CHOICES, verbose_name='Рейтинг')
    # # дата публикация
    # published = models.DateTimeField(auto_now_add=True, db_index=True,
    #                                  verbose_name='Опубликовано')
    #
    # class Meta:
    #     verbose_name_plural = 'Отзывы'
    #     verbose_name = 'Отзыв'
    #     ordering = ['-published']
