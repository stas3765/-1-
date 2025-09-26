# Структура проекта

order_project/
├── app/
│   ├── main.py
│   └── utils/
│       ├── __init__.py
│       └── check_data.py
├── tests/
│   └── test_check_data.py
├── requirements.txt
├── README.md
└── .gitignore

# Расчёт стоимости скрепок

Функция `check_total_cost` рассчитывает стоимость заказа скрепок по количеству с учётом скидок.

## Тарифы
- 1–100 шт.: 10 руб./шт.
- 101–200 шт.: 9 руб./шт.
- 201–300 шт.: 8 руб./шт.
- >300 шт.: 7 руб./шт.

## Запуск тестов

python -m pytest tests/ -v