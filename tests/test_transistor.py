import pytest

from components.transistor import (
    calculate_base_current,
    calculate_collector_current,
    calculate_transistor_power
)


def test_base_current():
    assert calculate_base_current(0.02, 100) == pytest.approx(0.0002)


def test_collector_current():
    assert calculate_collector_current(0.0002, 100) == pytest.approx(0.02)


def test_transistor_power():
    assert calculate_transistor_power(5, 0.02) == pytest.approx(0.1)


def test_zero_current_gain():
    with pytest.raises(ValueError):
        calculate_base_current(0.02, 0)


def test_negative_base_current():
    with pytest.raises(ValueError):
        calculate_collector_current(-0.001, 100)


def test_negative_voltage():
    with pytest.raises(ValueError):
        calculate_transistor_power(-5, 0.02)
