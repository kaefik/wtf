# Backend WTF

## Установка зависимостей для работы

```bash
pip install wheel -U
pip install uvicorn fastapi pydantic 
```

для PyCharm нужно установить плагин [Pydantic PyCharm Plugin](https://github.com/koxudaxi/pydantic-pycharm-plugin/) (File -> Settings -> Plugins -> Marketplace)


## Установка stubs для проверки типов

```bash
pip install mypy
pip install pandas-stubs
```

## Запуск приложения backend

```buildoutcfg
uvicorn main:app
```
