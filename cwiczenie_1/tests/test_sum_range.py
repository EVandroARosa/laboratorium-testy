import pytest
import sys
import os

# To rozwiązuje problemy z importem, jeśli PyCharm "nie widzi" folderu src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sum_range import sum_range

@pytest.mark.parametrize("a, b, oczekiwany", [
    (1, 5, 15), (0, 0, 0), (-3, 3, 0), (-5, -1, -15), (10, 10, 10),
    (1, 100, 5050), (0, 1, 1), (-1, 0, -1), (100, 200, 15150), (0, 10, 55)
])
def test_sum_range_parametryzowany(a, b, oczekiwany):
    assert sum_range(a, b) == oczekiwany

def test_wyjatki():
    with pytest.raises(ValueError):
        sum_range(10, 5)
    with pytest.raises(TypeError):
        sum_range(1.5, 5)