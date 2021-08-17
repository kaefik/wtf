# TODO

* в сущности Toilet и Comment нужно проработать id уникальный, возможно сделать генерацию id
* [Установка OpenStreetMap Nominatim для нахождения широты и долготы по введенному адресу](https://habr.com/ru/post/259667/)
* [Geopandas в Python](https://pythonim.ru/libraries/geopandas-v-python)
* 

```bash
    path('toilet/<int:pk>/comment/<int:c_pk>', CommentSingleAPIView.as_view(), name='get_single_comment'),
    path('toilet/<int:t_pk>/comment/<int:c_pk>/modify/', api_get_delete_update_comment,
         name='get_delete_update_comment'),
    path('toilet/<int:pk>/modify/', api_get_delete_update_toilet, name='get_delete_update_toilet'),
    path('toilet/add', api_add_toilet, name='add_toilet'),
    path('toilet/<int:pk>', ToiletDetailView.as_view(), name='get_single_detail_toilet'),
    path('toilets/', api_toilets, name='get_all_toilets'),
    path('toilet/<int:pk>/comments/', api_comments, name='get_all_comments_toilet'),
```