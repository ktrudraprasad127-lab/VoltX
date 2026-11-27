
from calculations.resistance import calculate_resistance


def test_brown_black_red_gold():
    resistance, tolerance = calculate_resistance(
        "brown", "black", "red", "gold"
    )

    assert resistance == 1000
    assert tolerance == 5


def test_red_red_brown_gold():
    resistance, tolerance = calculate_resistance(
        "red", "red", "brown", "gold"
    )

    assert resistance == 220
    assert tolerance == 5
