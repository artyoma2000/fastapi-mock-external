# 🚀 FastAPI Приложение с Имитацией Внешних Зависимостей

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-brightgreen)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

## 🎯 Особенности

- **Имитация внешних API**: Взаимодействие с внешними API и базами данных с использованием асинхронных запросов.
- **Асинхронность**: Применение асинхронных вызовов для повышения производительности.
- **Поддержка тестирования**: Написание тестов с использованием `pytest` и `unittest.mock` для подмены внешних зависимостей.
- **Современный FastAPI**: Использование современного фреймворка для создания высокопроизводительных API.

## 📂 Структура проекта

```
fastapi-mock-external/
│
├── main.py                # Основной файл приложения FastAPI
├── test-main.py           # Тесты для FastAPI приложения
├── requirements.txt       # Зависимости проекта
└── README.md              # Описание проекта
```

### `main.py`

Содержит реализацию FastAPI приложения с двумя основными конечными точками:
- `GET /data`: Получение данных из внешнего API.
- `POST /db`: Запись данных в базу данных.

### `test-main.py`

Содержит тесты для проверки взаимодействия с внешними зависимостями. Тесты используют `unittest.mock` для создания имитаций (моков) внешних функций.

### `requirements.txt`

Содержит список зависимостей для запуска приложения и выполнения тестов.

## 🚀 Начало работы

### Требования

- **Python 3.8+**

### Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/artyoma2000/fastapi-mock-external.git
    cd fastapi-mock-external
    ```

2. **Создайте и активируйте виртуальное окружение:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

### Запуск приложения

1. **Запустите сервер FastAPI:**

    ```bash
    uvicorn main:app --reload
    ```

2. **Откройте документацию API:**

    - Перейдите по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) для просмотра Swagger UI.
    - Или [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) для ReDoc.

## 🛠️ Использование

### API Эндпоинты

- **`GET /data`**: Получает данные из внешнего API.
  - Пример ответа: `{"key": "value"}`
- **`POST /db`**: Записывает данные в базу данных.
  - Пример запроса:
    ```http
    POST /db
    Content-Type: application/json

    {
      "key": "value"
    }
    ```
  - Пример ответа: `{"status": "success"}`

## 🧪 Тестирование

### Запуск тестов

1. **Установите зависимости для тестирования:**

    ```bash
    pip install pytest pytest-asyncio
    ```

2. **Запустите тесты:**

    ```bash
    pytest test_main.py
    ```

### Обзор тестов

- Тесты используют `unittest.mock.patch` для имитации внешних зависимостей:
  - **`fetch_external_data`**: Имитирует функцию получения данных из внешнего API.
  - **`write_to_database`**: Имитирует функцию записи данных в базу данных.

#### Пример кода теста

```python
import pytest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_data_success():
    with patch('main.fetch_external_data', new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = {"key": "value"}
        response = client.get("/data")
        assert response.status_code == 200
        assert response.json() == {"key": "value"}

# Подробнее о тестах см. в `test-main.py`
```


## 🤝 Вклад

Приветствуются любые предложения и улучшения! Создавайте issue или pull request для обсуждения.

