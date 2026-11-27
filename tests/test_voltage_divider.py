import pytest

from calculations.voltage_divider import calculate_voltage_divider


def test_voltage_divider():
    assert calculate_voltage_divider(12, 1000, 1000) == 6


def test_unequal_resistors():
    assert calculate_voltage_divider(12, 1000, 2000) == 8


def test_zero_resistance():
    with pytest.raises(ValueError):
        calculate_voltage_divider(12, 0, 1000)


def test_negative_voltage():
    with pytest.raises(ValueError):
        calculate_voltage_divider(-12, 1000, 1000)
        