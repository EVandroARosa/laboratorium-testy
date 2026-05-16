import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.roman import RomanNumeral

@pytest.mark.parametrize("arabic, roman", [
    (1, "I"), (4, "IV"), (9, "IX"), (10, "X"),
    (40, "XL"), (90, "XC"), (400, "CD"), (900, "CM"),
    (1994, "MCMXCIV"), (3999, "MMMCMXCIX")
])
def test_conversion(arabic, roman):
    assert RomanNumeral.to_roman(arabic) == roman

def test_out_of_range():
    with pytest.raises(ValueError):
        RomanNumeral.to_roman(4000)