# API Documentation & Testing Guide

Нижче наведено список запитів для перевірки роботи збережених процедур та тригерів.
**Base URL:** `http://127.0.0.1:5000`

---

## 1. Тестування Збережених Процедур

### 1.1. Пакетна генерація даних (Loop)
Створює 10 користувачів з іменами Noname1...Noname10.
* **Method:** `POST`
* **URL:** `/api/proc/generate-users`
* **Body:** (empty)

### 1.2. Створення зв'язку M:M за логічними іменами
Зв'язує юзера та станцію, знаючи лише Email та Назву станції (ID знаходяться автоматично в БД).
* **Method:** `POST`
* **URL:** `/api/proc/link-user-station`
* **JSON Body:**
    ```json
    {
        "email": "noname1@test.com",
        "station_name": "SolarHome1"
    }
    ```

### 1.3. Динамічна агрегація (Dynamic SQL)
Рахує MAX, MIN або AVG для будь-якого стовпця будь-якої таблиці.
* **Method:** `POST`
* **URL:** `/api/proc/aggregate`
* **JSON Body:**
    ```json
    {
        "table": "battery",
        "column": "capacity_kwh",
        "func": "AVG"
    }
    ```

### 1.4. Робота з курсором (Dynamic Tables)
Проходить курсором по типах панелей і створює під них нові таблиці.
* **Method:** `POST`
* **URL:** `/api/proc/create-dynamic-tables`
* **Body:** (empty)

---

## 2. Тестування Тригерів (Triggers)

### 2.1. Перевірка "Fake Foreign Key" (Insert Check)
Спроба додати запис у журнал для неіснуючої станції. Тригер має заблокувати операцію.
* **Method:** `POST`
* **URL:** `/api/proc/test/log`
* **JSON Body:**
    ```json
    {
        "station_id": 99999,
        "description": "Log for non-existent station"
    }
    ```
* **Expected Result:** `400 Bad Request` (Error: Station ID does not exist).

### 2.2. Заборона видалення (Delete Check)
Спроба видалити станцію, у якої є записи в журналі.
1. Спочатку створіть станцію та додайте їй лог (успішно).
2. Спробуйте видалити цю станцію:
* **Method:** `DELETE`
* **URL:** `/api/proc/test/station/{id}`
* **Expected Result:** `400 Bad Request` (Error: Cannot delete station: dependent records...).

### 2.3. Аудит видалення (Audit Log)
Перевірка запису в лог після успішного видалення.
1. Видаліть станцію без залежностей (успішно, 200 OK).
2. Перевірте таблицю аудиту:
* **Method:** `GET`
* **URL:** `/api/proc/test/audit`
* **Response:** JSON список видалених об'єктів.

### 2.4. Валідація даних (User Surname)
Спроба створити користувача з прізвищем, що закінчується на "00".
* **Method:** `POST`
* **URL:** `/users` (стандартний контролер)
* **JSON Body:**
    ```json
    {
        "name": "Test",
        "surname": "Bond00",
        "email": "agent00@test.com"
    }
    ```
* **Expected Result:** `400/500 Error` (Error: Surname cannot end with 00).