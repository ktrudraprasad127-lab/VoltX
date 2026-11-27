import pytest

from calculations.energy import (
    calculate_energy_joules,
    calculate_energy_kwh
)


def test_energy_joules():
    assert calculate_energy_joules(100, 10) == 1000


def test_energy_kwh():
    assert calculate_energy_kwh(1000, 2) == 2


def test_zero_power():
    assert calculate_energy_joules(0, 10) == 0


def test_negative_time():
    with pytest.raises(ValueError):
        calculate_energy_kwh(1000, -2)