import pytest

from calculations.capacitor import (
    calculate_charge,
    calculate_capacitance
)


def test_calculate_charge():
    assert calculate_charge(0.001, 12) == pytest.approx(0.012)


def test_calculate_capacitance():
    assert calculate_capacitance(0.012, 12) == pytest.approx(0.001)


def test_negative_capacitance():
    with pytest.raises(ValueError):
        calculate_charge(-0.001, 12)


def test_zero_voltage():
    with pytest.raises(ValueError):
        calculate_capacitance(0.012, 0)
        