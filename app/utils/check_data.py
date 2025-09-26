def check_total_cost(input_data: int) -> float:
    """
    Вычисляет общую стоимость заказа скрепок по количеству.
    
    Тарифы:
    - 1–100 шт.: 10 руб./шт.
    - 101–200 шт.: 9 руб./шт.
    - 201–300 шт.: 8 руб./шт.
    - >300 шт.: 7 руб./шт.

    :param input_data: количество скрепок (целое положительное число)
    :return: общая стоимость в рублях (float)
    :raises ValueError: при недопустимом значении
    """
    if not isinstance(input_data, int):
        raise ValueError("Количество не является числом")
    if input_data == 0:
        raise ValueError("Количество не может быть нулевым")
    if input_data < 0:
        raise ValueError("Количество должно быть положительным числом")

    if 1 <= input_data <= 100:
        return input_data * 10.0
    elif 101 <= input_data <= 200:
        return input_data * 9.0
    elif 201 <= input_data <= 300:
        return input_data * 8.0
    else:
        return input_data * 7.0