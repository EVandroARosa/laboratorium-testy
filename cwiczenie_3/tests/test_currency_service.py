import os
import sys

import pytest

# Ustawienie ścieżek dla importów
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.currency_service import CurrencyService

# Przykładowa odpowiedź API NBP
NBP_USD_RESPONSE = {
    "rates": [{"mid": 4.0832}]
}


def test_get_rate_z_mocker(mocker):
    """Sprawdza poprawne pobranie kursu USD przy użyciu mocker."""
    service = CurrencyService()
    mock_get = mocker.patch("requests.get")

    # Ustawiamy zachowanie mocka
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = NBP_USD_RESPONSE

    rate = service.get_rate("USD")
    assert rate == 4.0832
    mock_get.assert_called_once()


def test_get_rate_nieznana_waluta_rzuca_value_error(mocker):
    """Sprawdza, że błąd 404 powoduje rzucenie ValueError."""
    service = CurrencyService()
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 404

    # Tutaj był błąd - linia poniżej MUSI mieć wcięcie
    with pytest.raises(ValueError, match="Nieznana waluta"):
        service.get_rate("XYZ")