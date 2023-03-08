import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR))

try:
    from task32 import is_in_mass
except ModuleNotFoundError:
    assert False, 'Не найден файл с домашней работой `task32.py`'


def test_ordinary():
    s = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    mi = 5
    ma = 15
    assert is_in_mass(s, mi, ma) == [1, 9, 13, 14, 19], (
        'Стандартный тест падает, что-то не так'
        )


def test_borders():
    for j in range(4, 10000, 2):
        s = [i for i in range(j)]
        mi = j//2
        ma = j
        assert s[j//2::] == is_in_mass(s, mi, ma), (
            'Проблемы с учетом границы'
        )


def test_empty_search():
    for i in range(10000):
        s = [0 for j in range(i)]
        mi = 500
        ma = 1000
        assert is_in_mass(s, mi, ma) == [], (
            'Проблемы с отсутствием искомых чисел'
            )


def test_zeros():
    for j in range(10000):
        s = [0 for i in range(j)]
        mi = 0
        ma = 0
        res = [i for i in range(j)]
        assert is_in_mass(s, mi, ma) == res, (
            'Проблемы с нулями'
            )
