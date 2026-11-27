import pytest

from components.resistor import (
    calculate_resistor_power,
    calculate_resistor_voltage,
    calculate_resistor_current
)


def test_resistor_power():
    assert calculate_resistor_power(12, 6) == 24


def test_resistor_voltage():
    assert calculate_resistor_voltage(2, 10) == 20


def test_resistor_current():
    assert calculate_resistor_current(20, 10) == 2


def test_zero_resistance():
    with pytest.raises(ValueError):
        calculate_resistor_current(12, 0)


def test_negative_voltage():
    with pytest.raises(ValueError):
        calculate_resistor_power(-12, 6)


def test_negative_current():
    with pytest.raises(ValueError):
        calculate_resistor_voltage(-2, 10)
