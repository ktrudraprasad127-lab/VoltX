import pytest

from calculations.current_divider import calculate_current_divider


def test_current_divider():
    current_r1, current_r2 = calculate_current_divider(6, 2, 4)

    assert current_r1 == 4
    assert current_r2 == 2


def test_equal_resistances():
    current_r1, current_r2 = calculate_current_divider(10, 5, 5)

    assert current_r1 == 5
    assert current_r2 == 5


def test_zero_resistance():
    with pytest.raises(ValueError):
        calculate_current_divider(6, 0, 4)


def test_negative_current():
    with pytest.raises(ValueError):
        calculate_current_divider(-6, 2, 4)