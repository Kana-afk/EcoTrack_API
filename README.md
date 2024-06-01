# EcoTrack API

EcoTrack API - это платформа для мониторинга и управления данными о качестве воздуха с различных датчиков.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/yourusername/ecotrack-api.git
    cd ecotrack-api
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для MacOS/Linux
    .\venv\Scripts\activate   # Для Windows
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции:

    ```bash
    python manage.py migrate
    ```

5. Создайте суперпользователя:

    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

## API Эндпоинты

### Регистрация пользователя

- **URL:** `POST /api/auth/register/`
- **Body (JSON):**

    ```json
    {
        "username": "newuser",
        "password": "ComplexPass123!",
        "password2": "ComplexPass123!",
        "email": "newuser@example.com",
        "first_name": "New",
        "last_name": "User"
    }
    ```

### Вход пользователя

- **URL:** `POST /api/auth/login/`
- **Body (JSON):**

    ```json
    {
        "username": "newuser",
        "password": "ComplexPass123!"
    }
    ```

### Создание датчика

- **URL:** `POST /api/sensors/`
- **Headers:** `Authorization: Bearer <your_access_token>`
- **Body (JSON):**

    ```json
    {
        "type": "NO2",
        "model": "ABC456",
        "installation_date": "2024-01-15",
        "status": "active"
    }
    ```

### Получение списка датчиков

- **URL:** `GET /api/sensors/`
- **Headers:** `Authorization: Bearer <your_access_token>`

### Создание данных

- **URL:** `POST /api/data/`
- **Headers:** `Authorization: Bearer <your_access_token>`
- **Body (JSON):**

    ```json
    {
        "sensor": 2,
        "timestamp": "2024-01-15T14:30:00Z",
        "pm25": 10.25,
        "pm10": 20.50,
        "co2": 400.00
    }
    ```

### Создание оповещения

- **URL:** `POST /api/alerts/`
- **Headers:** `Authorization: Bearer <your_access_token>`
- **Body (JSON):**

    ```json
    {
        "sensor": 2,
        "timestamp": "2024-01-15T15:00:00Z",
        "description": "High NO2 levels detected"
    }
    ```

## Документация API

Документация доступна по адресу `/swagger/` и `/redoc/`.

