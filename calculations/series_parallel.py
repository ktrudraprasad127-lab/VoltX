def calculate_series_resistance(resistances):
    """
    Series resistance:
    R = R1 + R2 + R3 + ...
    """

    if not resistances or any(r <= 0 for r in resistances):
        raise ValueError("All resistances must be positive.")

    return sum(resistances)


def calculate_parallel_resistance(resistances):
    """
    Parallel resistance:
    1/R = 1/R1 + 1/R2 + 1/R3 + ...
    """

    if not resistances or any(r <= 0 for r in resistances):
        raise ValueError("All resistances must be positive.")

    return 1 / sum(1 / r for r in resistances)