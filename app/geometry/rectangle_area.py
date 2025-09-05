from typing import Union


def parse_number(value: str) -> float:
    """
    Проверка корректности ввода стороны прямоугольника.

    :param value: пользовательский ввод длины стороны прямоугольника
    :return: длина стороны прямоугольника (тип float)
    :raises ValueError: если значение не число или <= 0
    """
    if not value or not value.strip():
        raise ValueError("Сторона не может быть пустой")

    try:
        input_data = value.strip().replace(',', '.')
        number = float(input_data)
        if number <= 0:
            raise ValueError("Сторона должна быть положительным числом")
        return number
    except ValueError as e:
        if "could not convert string" in str(e):
            raise ValueError("Введено не числовое значение стороны")
        raise


def rectangle_area(width: str, height: str) -> float:
    """
    Вычисление площади прямоугольника.

    :param width: ширина прямоугольника (в виде строки)
    :param height: высота прямоугольника (в виде строки)
    :return: площадь прямоугольника
    :raises ValueError: если параметры некорректны
    """
    w = parse_number(width)
    h = parse_number(height)
    return w * h