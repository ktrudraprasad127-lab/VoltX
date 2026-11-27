import pytest

from calculations.series_parallel import (
    calculate_series_resistance,
    calculate_parallel_resistance
)


def test_series_resistance():
    assert calculate_series_resistance([10, 20, 30]) == 60


def test_parallel_resistance():
    assert calculate_parallel_resistance([10, 20, 30]) == pytest.approx(5.454545)


def test_single_resistor_series():
    assert calculate_series_resistance([100]) == 100


def test_empty_resistance_list():
    with pytest.raises(ValueError):
        calculate_parallel_resistance([])


def test_zero_resistance():
    with pytest.raises(ValueError):
        calculate_series_resistance([10, 0, 20])