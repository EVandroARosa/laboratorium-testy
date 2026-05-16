import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculator import Calculator

@pytest.fixture
def calc():
    """Nowy kalkulator dla każdego testu (function scope)."""
    return Calculator()

@pytest.fixture(scope="module")
def calc_with_history():
    """Kalkulator z historią współdzielony w module."""
    c = Calculator()
    c.add(10, 5)
    c.subtract(10, 3)
    return c