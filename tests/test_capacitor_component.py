import pytest

from components.capacitor import (
    calculate_capacitor_energy,
    calculate_capacitive_reactance
)


def test_capacitor_energy():
    assert calculate_capacitor_energy(0.001, 12) == pytest.approx(0.072)


def test_zero_voltage_energy():
    assert calculate_capacitor_energy(0.001, 0) == 0


def test_invalid_capacitance():
    with pytest.raises(ValueError):
        calculate_capacitor_energy(0, 12)


def test_capacitive_reactance():
    assert calculate_capacitive_reactance(50, 0.0001) == pytest.approx(31.831, rel=1e-3)


def test_zero_frequency():
    with pytest.raises(ValueError):
        calculate_capacitive_reactance(0, 0.0001)


def test_negative_capacitance():
    with pytest.raises(ValueError):
        calculate_capacitive_reactance(50, -0.0001)
