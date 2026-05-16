# Ćwiczenie 2: Testowanie operacji na bazie danych (CRUD)

## Opis
Projekt testuje klasę `UserRepository` zarządzającą użytkownikami w bazie SQLite. Wykorzystano bazę danych w pamięci (`:memory:`), co zapewnia szybkość i czystość testów.

## Wykorzystane mechanizmy
- **Pytest Fixtures**: `repo` (zakres funkcyjny) oraz `repo_with_data` (zakres modułowy).
- **Izolacja**: Każdy test korzysta z nowej instancji bazy.

## Instrukcja
Aby uruchomić testy i sprawdzić pokrycie:
```bash
pytest --cov=src --cov-report term-missing