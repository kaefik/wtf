"""
тестирование API
"""

import requests
import json

from typing import Dict


def test_get():
    url_get = "http://127.0.0.1:8000/get"
    s = requests.Session()
    params = {"id": 0}
    result = s.get(url_get) #, params=params)
    return result


def test_add(data: Dict[str, str]):
    """

    :param data: { "author": "user", "text": "Hello!" }
    :return:
    """
    url_add = "http://127.0.0.1:8000/add"
    s = requests.Session()
    result = s.post(url_add, data=json.dumps(data))
    return result


def test_delete(id: int):
    """

    :param id - номер
    :return:
    """
    url_delete = "http://127.0.0.1:8000/delete"
    params = {"id": id}
    s = requests.Session()
    result = s.delete(url_delete, params=params)
    return result


if __name__ == "__main__":
    r = test_get()

    # r = test_delete(1)

    # --------------
    # data = {
    #     "author": "user",
    #     "text": "Hello!"
    # }
    # r = test_add(data)

    # --------------

    print(r.headers)
    print(r.status_code)
    print(r.content)
