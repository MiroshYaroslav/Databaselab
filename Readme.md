# Solar Station API

Проект реалізує Back-End для бази даних `solar_station` з використанням **Flask + Python + MySQL**.  
API підтримує CRUD операції для всіх таблиць та дозволяє працювати із зв’язками M:1 та M:M.

## Особливості

- Управління користувачами (`User`) та їхніми станціями (`Station`).
- Збереження інформації про адреси (`Address`) для станцій.
- Облік сонячних панелей (`Panel`), батарей (`Battery`) та їх характеристик.
- Реєстрація генерації енергії (`PanelGeneration`) та продажів енергії (`EnergySale`).
- Автоматичне формування зв’язків між користувачами та станціями через проміжну таблицю M:M.
- Використання **Flask Blueprints** для логічного розділення API по модулях.
- Генералізовані маршрути (`generic_bp`) для швидкого додавання нових моделей без створення окремого Blueprint.

## Використані технології

- Python 3.x  
- Flask  
- Flask-SQLAlchemy  
- Flask-Marshmallow  
- MySQL  
- Marshmallow для серіалізації/десеріалізації даних  

## Інструкція по запуску

1. Клонувати репозиторій:
    ```bash
    git clone <repository-url>
    cd solar_station_api
    ```

2. Створити та активувати віртуальне середовище:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Встановити залежності:
    ```bash
    pip install -r requirements.txt
    ```

4. Налаштувати підключення до MySQL у файлі конфігурації (`config.py`).

5. Запустити сервер:
    ```bash
    flask run
    ```

API буде доступне за адресою: `http://127.0.0.1:5000`

## Документація API

Всі маршрути та їх призначення описані у файлі `API_ROUTES.md` (або окремому файлі зі списком запитів).  
API підтримує стандартні методи: `GET`, `POST`, `PUT`, `DELETE`, `OPTIONS`, `HEAD`.

## Приклад запиту

Отримати всі станції користувача з `id=3`:

```http
GET /api/users/3/stations
