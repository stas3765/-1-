import pytest
from app.utils.check_data import check_total_cost


valid_cases = [
    # Диапазон 1–100
    (1, 10.0),
    (50, 500.0),
    (100, 1000.0),

    # Диапазон 101–200
    (101, 909.0),
    (150, 1350.0),
    (200, 1800.0),

    # Диапазон 201–300
    (201, 1608.0),
    (250, 2000.0),
    (300, 2400.0),

    # Диапазон >300
    (301, 2107.0),
    (350, 2450.0),
    (400, 2800.0),
]


invalid_cases = [
    (0, "Количество не может быть нулевым"),
    (-1, "Количество должно быть положительным числом"),
    (-100, "Количество должно быть положительным числом"),
    ("ghg", "Количество не является числом"),
    (3.14, "Количество не является числом"),
    (None, "Количество не является числом"),
    ([], "Количество не является числом"),
]


@pytest.mark.parametrize("quantity, expected", valid_cases)
def test_check_total_cost_valid(quantity, expected):
    assert check_total_cost(quantity) == expected


@pytest.mark.parametrize("quantity, expected_msg", invalid_cases)
def test_check_total_cost_invalid(quantity, expected_msg):
    with pytest.raises(ValueError) as exc_info:
        check_total_cost(quantity)
    assert str(exc_info.value) == expected_msg