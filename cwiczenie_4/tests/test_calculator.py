import pytest

def test_dodawanie(calc):
    assert calc.add(2, 3) == 5

def test_dzielenie_przez_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)

def test_historia_zawiera_wpisy(calc_with_history):
    assert len(calc_with_history.get_history()) >= 2