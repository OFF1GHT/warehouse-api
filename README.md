#  Проект: API для управления складом

### Описание проета
Данный проект представляет собой REST API для управления складом с использованием FastAPI и SQLAlchemy. С помощью API можно управлять товарами, отслеживать складские запасы и заказы. Реализованы основные операции для работы с товарами и заказами, а также бизнес-логика для создания заказов с проверкой наличия товаров на складе.

### Установка и запуск
1. Клонируте репозиторий:
```
git clone git@github.com:OFF1GHT/warehouse-api.git
cd stockroom
```

2. Создайте и активируйте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # для Windows используйте venv\Scripts\activate
```

3. Установите зависимости:
```
pip install -r requirements.txt
```

4. Создайте файл .env:
```
# Пример файла .env
DATABASE_URL=postgresql+asyncpg://user:password@db/rooom
SECRET_KEY=mysecretkey
DEBUG=True
```

5. Запуск приложения через Docker:
```
docker-compose up --build
```

6. Выполните миграции в контейнере:
```
alembic upgrade head
```

7. Приложение будет доступно по адресу: http://localhost:8000

### Документация 
Интерактивная документация API доступна по следующим адресам:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Технологии
- Python: Основной язык разработки.
- FastAPI: Фреймворк для создания веб-приложений.
- SQLAlchemy (v2): ORM для работы с базой данных.
- PostgreSQL: База данных для хранения информации о товарах и заказах.
- Docker: Используется для контейнеризации приложения.
- Docker Compose: Для сборки и управления сервисами (включая базу данных).