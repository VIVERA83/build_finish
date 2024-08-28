# <span style="color:orange">Build finish (Строй отделка)</span>

## <span style="color:purple">Тестовое задание.</span>

__Общая информация:__ Вам необходимо разработать REST API для управления продуктами на торговой площадке.

__API должно позволять пользователям:__

- <span style="color:green">добавлять</span>
- <span style="color:green">обновлять</span>
- <span style="color:green">удалять</span>
- <span style="color:green">получать информацию о продуктах</span>
- <span style="color:green">получать информацию о категориях</span>
- <span style="color:green">фильтровать продукты по различным параметрам</span>

#### Требования к решению:

1. __Обязательные технические требования:__
    - <span style="color:green">оформлена инструкция по запуску сервиса
      и взаимодействия с проектом(Markdown по необходимости)</span>
    - <span style="color:green">сервис реализован с использованием FastAPI</span>
2. __Необязательные технические требования (по возрастанию трудоемкости):__
    - <span style="color:green">использовать можно любые БД (реляционные, не реляционные), как и способ доступа и
      управления данными внутри (сырые sql или orm, если выбрали реляционную модель)</span>
    - <span style="color:green">зависимости зафиксированы менеджером зависимостей poetry</span>
    - написаны тесты с использованием pytest
    - <span style="color:green">реализована возможность собирать и запускать контейнер с сервисом docker</span>

## <span style="color:purple">Запуск приложения</span>

Swagger документация доступна по адресу: __http://127.0.0.1:8008/docs__, при условии,
что переменные окружения были взяты из [example.env](example.env)

#### Запуск с помощью Docker

1. Необходимо создать файл в котором будут находиться переменные окружения, для тестового запуска
   приложения можно воспользоваться [example.env](example.env), достаточно переименовать в ```.env```
2. выполнить команду для запуска Docker контейнера, со всем необходимыми зависимостями.
      ```bash
   docker compose up --build -d
   ```

#### Запуск на локальной машине

1. Необходимо создать файл в котором будут находиться переменные окружения,
   для тестового запуска приложения можно воспользоваться [example.env](example.env), достаточно переименовать в
   ```.env```

   Обратите внимание на строчки в env файле:
    - __POSTGRES_HOST="postgres"__ в место <span style="color:red">"postgres"</span> необходимо указать адрес до БД
      Postgres
      Если она установлена на том же ПК то обычно это адрес: <span style="color:red">"127.0.0.1"</span>
    - __POSTGRES_PORT="5447"__ в место <span style="color:red">"5447"</span> необходимо указать порт БД Postgres
      По умолчанию это: <span style="color:red">"5432"</span>
    - __POSTGRES_DB="test_db"__ в место <span style="color:red">"test_db"</span> необходимо указать имя БД
      По умолчанию это: <span style="color:red">"postgres"</span>
    - __POSTGRES_USER="test_user"__ в место <span style="color:red">"test_user"</span> необходимо указать имя
      пользователя которое Вы используете для подключения к БД
    - __POSTGRES_PASSWORD="test_pass"__ в место <span style="color:red">"test_pass"</span> необходимо указать пароль
      который Вы используете для подключения к БД
    - __HOST="app"__ в место <span style="color:red">"app"</span> необходимо указать <span style="color:red">"
      127.0.0.1"</span>


2. Устанавливаем зависимости.
    - Необходимо установить [poetry](https://python-poetry.org/) если не установлен.
       ```bash
       pip install poetry   
       ```
    - Устанавливаем необходимые зависимости для проекта. Из корневого каталога запускаем:
      ```bash
      poetry install
      ```  
   3. Устанавливаем миграции для БД
      ```bash
      poetry run alembic upgrade head
      ```
4. Запускаем проект:
    - переходим в каталог [build_finish](build_finish) где находится [main.py](build_finish/main.py)
      ```bash
      cd build_finish
      ```
    - запускаем
      ```bash
      poetry run python main.py
      ```

## <span style="color:purple">Вспомогательные команды</span>

- Инициализация таблиц

```bash
alembic revision --autogenerate -m "Initial tables"
```

- Обновления таблиц в БД

```bash
alembic upgrade head
```

