
import pytest

from calculations.ohms_law import (
    calculate_voltage,
    calculate_current,
    calculate_resistance
)


def test_calculate_voltage():
    assert calculate_voltage(2, 10) == 20


def test_calculate_current():
    assert calculate_current(20, 10) == 2


def test_calculate_resistance():
    assert calculate_resistance(20, 2) == 10


def test_zero_resistance():
    with pytest.raises(ValueError):
        calculate_current(20, 0)


def test_zero_current():
    with pytest.raises(ValueError):
        calculate_resistance(20, 0)
    