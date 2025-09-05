import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.geometry.rectangle_area import rectangle_area


def test_rectangle_area_correct_length():
    width = "3"
    height = "5"
    expected_result = 15.0
    result = rectangle_area(width, height)
    assert result == pytest.approx(expected_result)
    # Act
    actual_result = rectangle_area(width, height)

    # Assert
    assert actual_result == pytest.approx(expected_result)
    











    import sys
import os
import pytest

# Добавляем путь к корню проекта, чтобы импорт работал
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.geometry.rectangle_area import rectangle_area


def test_rectangle_area_string_data():
    """
    Тестирование вычисления площади со строкой в качестве стороны прямоугольника.
    Ожидается ValueError с сообщением "Введено не числовое значение стороны"
    """
    # Arrange — подготовка данных
    width = "hello"  # Некорректная сторона (строка)
    height = "5.2"   # Корректная высота

    # Act — вызов тестируемого кода
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)

    # Assert — проверка результата
    assert str(exc_info.value) == "Введено не числовое значение стороны"

def test_rectangle_area_decimal_values():
    """
    Тест: стороны заданы десятичными дробями (через точку)
    """
    # Arrange
    width = "2.5"
    height = "4.0"
    expected_result = 10.0

    # Act
    actual_result = rectangle_area(width, height)

    # Assert
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_comma_separated_values():
    """
    Тест: стороны заданы с использованием запятой как десятичного разделителя
    """
    # Arrange
    width = "1,5"
    height = "2,0"
    expected_result = 3.0

    # Act
    actual_result = rectangle_area(width, height)

    # Assert
    assert actual_result == pytest.approx(expected_result)


def test_rectangle_area_large_integers():
    """
    Тест: большие целые числа
    """
    # Arrange
    width = "100"
    height = "250"
    expected_result = 25000.0

    # Act
    actual_result = rectangle_area(width, height)

    # Assert
    assert actual_result == pytest.approx(expected_result)