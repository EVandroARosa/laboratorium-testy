from unittest.mock import patch, mock_open
import pytest
import sys
import os

# Poprawka ścieżek
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.file_logger import FileLogger

def test_log_otwiera_plik_do_zapisu():
    """Sprawdza, czy log() otwiera plik w trybie dopisywania ('a')[cite: 1155, 1156]."""
    logger = FileLogger("test.log")
    m = mock_open()
    with patch("builtins.open", m):
        logger.log("Test message")
    m.assert_called_once_with("test.log", "a", encoding="utf-8")

def test_read_logs_zwraca_puste_gdy_brak_pliku():
    """Sprawdza, że read_logs() zwraca [] gdy plik nie istnieje[cite: 1178, 1179]."""
    logger = FileLogger("nieistniejacy.log")
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = logger.read_logs()
    assert result == []