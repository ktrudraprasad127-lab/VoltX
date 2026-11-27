import pytest

from calculations.power import (
    calculate_power_voltage_current,
    calculate_power_current_resistance,
    calculate_power_voltage_resistance
)


def test_power_voltage_current():
    assert calculate_power_voltage_current(12, 2) == 24


def test_power_current_resistance():
    assert calculate_power_current_resistance(2, 6) == 24


def test_power_voltage_resistance():
    assert calculate_power_voltage_resistance(12, 6) == 24


def test_zero_resistance():
    with pytest.raises(ValueError):
        calculate_power_voltage_resistance(12, 0)