## Тестування Тригерів (SQL Scenarios)

### Сценарій 1: Емуляція Foreign Key (Цілісність даних)
**Мета:** Перевірити, чи забороняє тригер вставку записів, якщо батьківського об'єкта не існує.

```sql
-- 1.1. Спроба додати запис у журнал для неіснуючої станції (ID = 999999)
-- ОЧІКУВАНИЙ РЕЗУЛЬТАТ:  Error Code: 1644. Station ID does not exist.
INSERT INTO `maintenance_logs` (`station_id`, `description`) 
VALUES (999999, 'Test Log: Invalid Station');
```
Сценарій 2: Захист від видалення (Data Dependency)
Мета: Перевірити, чи забороняє тригер видалення батьківського запису, якщо існують залежні записи.

```sql
-- 2.1. Створюємо тимчасову станцію
INSERT INTO `station` (`name`) VALUES ('Station Protected By Trigger');
SET @prot_station_id = LAST_INSERT_ID();
```

```sql
-- 2.2. Додаємо до неї запис у журнал (Успішно)
INSERT INTO `maintenance_logs` (`station_id`, `description`) 
VALUES (@prot_station_id, 'Log prevents deletion');
```

```sql

-- 2.3. Спроба видалити цю станцію
-- ОЧІКУВАНИЙ РЕЗУЛЬТАТ:  Error Code: 1644. Cannot delete station: dependent records...
DELETE FROM `station` WHERE `id` = @prot_station_id;
```

Сценарій 3: Аудит видалення (Audit Log)
Мета: Перевірити, чи записується факт видалення у таблицю аудиту.

```sql
-- 3.1. Створюємо станцію без залежностей
INSERT INTO `station` (`name`) VALUES ('Station For Audit Test');
SET @audit_station_id = LAST_INSERT_ID();

-- 3.2. Видаляємо її (Успішно, бо немає логів)
-- ОЧІКУВАНИЙ РЕЗУЛЬТАТ: 1 row affected.
DELETE FROM `station` WHERE `id` = @audit_station_id;

-- 3.3. Перевіряємо таблицю `audit_log_deleted`
-- ОЧІКУВАНИЙ РЕЗУЛЬТАТ: Бачимо ID видаленої станції та час видалення.
SELECT * FROM `audit_log_deleted` ORDER BY `id` DESC LIMIT 5;
```
Сценарій 4: Валідація бізнес-правил
Мета: Перевірити заборону на специфічні формати даних (наприклад, прізвище не може закінчуватися на "00").

```sql
-- 4.1. Спроба зареєструвати користувача з прізвищем, що закінчується на "00"
-- ОЧІКУВАНИЙ РЕЗУЛЬТАТ: Error Code: 1644. Surname cannot end with 00.
INSERT INTO `user` (`name`, `surname`, `email`) 
VALUES ('James', 'Bond00', '007@test.com');

-- 4.2. Реєстрація коректного користувача
-- ОЧІКУВАНИЙ РЕЗУЛЬТАТ: 1 row affected.
INSERT INTO `user` (`name`, `surname`, `email`) 
VALUES ('James', 'Bond', 'valid_agent@test.com');
```