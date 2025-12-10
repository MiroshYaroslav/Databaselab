# API Запити
| Метод              | URL                                 | Опис                                                |
| ------------------ | ----------------------------------- |-----------------------------------------------------|
| HEAD, GET, OPTIONS | `/api/users`                        | Повертає список усіх користувачів.                  |
| HEAD, GET, OPTIONS | `/api/users/<int:user_id>`          | Повертає одного користувача за ID.                  |
| POST, OPTIONS      | `/api/users`                        | Створює нового користувача.                         |
| PUT, OPTIONS       | `/api/users/<int:user_id>`          | Оновлює дані користувача за ID.                     |
| DELETE, OPTIONS    | `/api/users/<int:user_id>`          | Видаляє користувача за ID.                          |
| HEAD, GET, OPTIONS | `/api/users/<int:user_id>/stations` | M:M Повертає всі станції, пов’язані з користувачем. |


| Метод              | URL                                      | Опис                                                    |
| ------------------ | ---------------------------------------- |---------------------------------------------------------|
| HEAD, GET, OPTIONS | `/api/stations`                          | Повертає список усіх станцій.                           |
| HEAD, GET, OPTIONS | `/api/stations/<int:station_id>`         | Повертає одну станцію за ID.                            |
| POST, OPTIONS      | `/api/stations`                          | Створює нову станцію.                                   |
| PUT, OPTIONS       | `/api/stations/<int:station_id>`         | Оновлює станцію за ID.                                  |
| DELETE, OPTIONS    | `/api/stations/<int:station_id>`         | Видаляє станцію за ID.                                  |
| HEAD, GET, OPTIONS | `/api/stations/<int:station_id>/address` | M:1 Повертає адресу станції.                            |
| HEAD, GET, OPTIONS | `/api/stations/<int:station_id>/users`   | M:M Повертає всіх користувачів, пов’язаних зі станцією. |


| Метод              | URL                                     | Опис                                                                           |
| ------------------ | --------------------------------------- |--------------------------------------------------------------------------------|
| HEAD, GET, OPTIONS | `/api/addresses`                        | Повертає список усіх адрес.                                                    |
| HEAD, GET, OPTIONS | `/api/addresses/<int:address_id>`       | Повертає адресу за ID.                                                         |
| POST, OPTIONS      | `/api/addresses`                        | Створює нову адресу.                                                           |
| PUT, OPTIONS       | `/api/addresses/<int:address_id>`       | Оновлює адресу за ID.                                                          |
| DELETE, OPTIONS    | `/api/addresses/<int:address_id>`       | Видаляє адресу за ID.                                                          |
| HEAD, GET, OPTIONS | `/api/addresses/<int:address_id>/users` | M:1 Повертає всіх користувачів, які живуть за цією адресою (якщо прив’язка є). |


| Метод              | URL                                    | Опис                            |
| ------------------ | -------------------------------------- | ------------------------------- |
| HEAD, GET, OPTIONS | `/api/panel-types`                     | Повертає всі типи панелей.      |
| HEAD, GET, OPTIONS | `/api/panel-types/<int:panel_type_id>` | Повертає конкретний тип панелі. |
| POST, OPTIONS      | `/api/panel-types`                     | Створює новий тип панелі.       |
| PUT, OPTIONS       | `/api/panel-types/<int:panel_type_id>` | Оновлює тип панелі.             |
| DELETE, OPTIONS    | `/api/panel-types/<int:panel_type_id>` | Видаляє тип панелі.             |


| Метод              | URL                                  | Опис                                           |
| ------------------ | ------------------------------------ |------------------------------------------------|
| HEAD, GET, OPTIONS | `/api/panels`                        | Повертає список усіх панелей.                  |
| HEAD, GET, OPTIONS | `/api/panels/<int:panel_id>`         | Повертає конкретну панель.                     |
| POST, OPTIONS      | `/api/panels`                        | Створює нову панель.                           |
| PUT, OPTIONS       | `/api/panels/<int:panel_id>`         | Оновлює панель.                                |
| DELETE, OPTIONS    | `/api/panels/<int:panel_id>`         | Видаляє панель.                                |
| HEAD, GET, OPTIONS | `/api/panels/<int:panel_id>/station` | M:1 Повертає станцію, до якої належить панель. |
| HEAD, GET, OPTIONS | `/api/panels/<int:panel_id>/type`    | M:1 Повертає тип панелі.                       |


| Метод              | URL                                       | Опис                                            |
| ------------------ | ----------------------------------------- |-------------------------------------------------|
| HEAD, GET, OPTIONS | `/api/batteries`                          | Повертає всі батареї.                           |
| HEAD, GET, OPTIONS | `/api/batteries/<int:battery_id>`         | Повертає батарею за ID.                         |
| POST, OPTIONS      | `/api/batteries`                          | Створює батарею.                                |
| PUT, OPTIONS       | `/api/batteries/<int:battery_id>`         | Оновлює батарею.                                |
| DELETE, OPTIONS    | `/api/batteries/<int:battery_id>`         | Видаляє батарею.                                |
| HEAD, GET, OPTIONS | `/api/batteries/<int:battery_id>/station` | M:1 Повертає станцію, до якої належить батарея. |
| HEAD, GET, OPTIONS | `/api/batteries/<int:battery_id>/charges` | M:M Повертає всі заряди батареї.                |


| Метод              | URL                                                | Опис                                             |
| ------------------ | -------------------------------------------------- |--------------------------------------------------|
| HEAD, GET, OPTIONS | `/api/panel-generations`                           | Повертає всі покоління панелей.                  |
| HEAD, GET, OPTIONS | `/api/panel-generations/<int:generation_id>`       | Повертає конкретне покоління панелі.             |
| POST, OPTIONS      | `/api/panel-generations`                           | Створює нове покоління панелі.                   |
| PUT, OPTIONS       | `/api/panel-generations/<int:generation_id>`       | Оновлює покоління панелі.                        |
| DELETE, OPTIONS    | `/api/panel-generations/<int:generation_id>`       | Видаляє покоління панелі.                        |
| HEAD, GET, OPTIONS | `/api/panel-generations/<int:generation_id>/panel` | M:1 Повертає панель, до якої належить покоління. |


| Метод              | URL                                            | Опис                                          |
| ------------------ | ---------------------------------------------- |-----------------------------------------------|
| HEAD, GET, OPTIONS | `/api/battery-charges`                         | Повертає всі заряди батарей.                  |
| HEAD, GET, OPTIONS | `/api/battery-charges/<int:charge_id>`         | Повертає конкретний заряд батареї.            |
| POST, OPTIONS      | `/api/battery-charges`                         | Створює заряд батареї.                        |
| PUT, OPTIONS       | `/api/battery-charges/<int:charge_id>`         | Оновлює заряд батареї.                        |
| DELETE, OPTIONS    | `/api/battery-charges/<int:charge_id>`         | Видаляє заряд батареї.                        |
| HEAD, GET, OPTIONS | `/api/battery-charges/<int:charge_id>/battery` | M:1 Повертає батарею, до якої належить заряд. |


| Метод              | URL                                       | Опис                                           |
| ------------------ | ----------------------------------------- |------------------------------------------------|
| HEAD, GET, OPTIONS | `/api/energy-sales`                       | Повертає всі продажі енергії.                  |
| HEAD, GET, OPTIONS | `/api/energy-sales/<int:sale_id>`         | Повертає конкретний продаж енергії.            |
| POST, OPTIONS      | `/api/energy-sales`                       | Створює новий продаж енергії.                  |
| PUT, OPTIONS       | `/api/energy-sales/<int:sale_id>`         | Оновлює продаж енергії.                        |
| DELETE, OPTIONS    | `/api/energy-sales/<int:sale_id>`         | Видаляє продаж енергії.                        |
| HEAD, GET, OPTIONS | `/api/energy-sales/<int:sale_id>/station` | M:1 Повертає станцію, до якої належить продаж. |


