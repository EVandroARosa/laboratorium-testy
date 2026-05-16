def sum_range(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Argumenty muszą być liczbami całkowitymi.")
    if a > b:
        raise ValueError(f"Argument a ({a}) nie może być większy niż b ({b}).")
    return sum(range(a, b + 1))