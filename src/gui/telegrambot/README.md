# Телеграмм бот является GUI для WTF

О проекте

Данный телеграмм бот является интерфейсом для бэкенда WTF.

Основан на проекте [py-tlgbotcore](https://github.com/kaefik/py-tlgbotcore)

## Реализованные возможности:


## Плагины которые доступны:

1. **_core.py** - плагин, который реализует административные команды по плагинам и доступу к боту. Доступ имеет
   администраторы.

Полную документацию по модулю _core смотрите файл tlbotcore/_core.md

## Настройка проекта для запуска

### Библиотеки:

 ```bash
  pip3 install Telethon
  ```

### Конфигурационные файлы проекта:

* **config.py** - за основу можно взять файл config-example.py

  ```
    # здесь указывается переменные для запуска телеграмм бота
    TLG_APP_NAME = "tlgbotappexample"  # APP NAME get from https://my.telegram.org
    TLG_APP_API_ID = 1258887  # APP API ID get from https://my.telegram.org
    TLG_APP_API_HASH = "sdsadsadasd45522665f"  # APP API HASH get from https://my.telegram.org
    I_BOT_TOKEN = "0000000000:sfdfdsfsdf5s5541sd2f1sd5"  # TOKEN Bot from BotFather
    TLG_ADMIN_ID_CLIENT = [1258889]  # admin clients for admin telegram bot
    # proxy for Telegram
    TLG_PROXY_SERVER = None  # address MTProxy Telegram
    TLG_PROXY_PORT = None  # port  MTProxy Telegram
    TLG_PROXY_KEY = None  # secret key  MTProxy Telegram
    # for save settings user
    # CSV - сохранение данных настроек для доступа к боту используя БД в формате CSV
    # SQLITE - сохранение данных настроек для доступа к боту используя БД в формате sqlite3
    TYPE_DB = "SQLITE"
  ```

Параметром **TYPE_DB** можно выбрать сохранять настройки с помощью sqlite3 или в файле csv (бывает полезно когда по
каким-то причинам на устройстве нет встроенной библиотеки slite3)

### Запуск проекта:

```bash
python start_telegrambot.py
```


Структура папок проекта:
* папка images - вспомогательные изображения для настройки бота, в частности находится иконка для бота 
(<a href='https://ru.freepik.com/photos/paper'>Paper фото создан(а) freepik - ru.freepik.com</a>)
* 
