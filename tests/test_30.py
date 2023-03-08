import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR))

try:
    from task30 import arithmetic_progression
except ModuleNotFoundError:
    assert False, 'Не найден файл с домашней работой `task30.py`'


def test_ordinary():
    assert arithmetic_progression(7, 2, 5) == [7, 9, 11, 13, 15], (
        'Стандартный тест падает, что-то не так'
        )


def test_negative():
    assert arithmetic_progression(-1, -2, 3) == [-1, -3, -5], (
        'Проблемы с отрицательными'
        )


def test_start():
    for i in range(1000):
        assert arithmetic_progression(i, 22, 100)[0] == i, (
            'Начинается не с того числа'
            )


def test_len():
    for i in range(1000):
        assert len(arithmetic_progression(-1, -2, i)) == i, (
            'Начинается не с того числа'
            )


def test_zeros():
    assert arithmetic_progression(0, 0, 0) == [], (
        'Проблемы с Нулями'
        )


def test_zero_diff():
    for i in range(1000):
        assert arithmetic_progression(i, 0, 4) == [i, i, i, i], (
            'Проблемы с нулевой разностью'
            )
