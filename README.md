
Web-приложение для определения заполненных форм.

#### Стек технологий:
- Python3.11
- MongoDB - СУБД
- FastAPI - API
- Docker

#### Запуск приложения

- Копируем код приложения в Вашу директорию.

`https://github.com/KIchkinevVladislav/forms_test`

- Запускаем контейнеры

`docker compose up -d`

- Заполняем бд

`docker exec forms_app python insert_mongo_data.py`

Приложение готово для тестирования:

http://127.0.0.1:8000/docs

#### Запуск тестов

`docker exec forms_app python -m unittest`

#### Запуск тестов для взаимодействия с запущеннум приложением

`docker exec forms_app python test_script.py`