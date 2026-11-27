import math
import pytest

from signal_analysis.waveform import (
    generate_sine_wave,
    generate_square_wave,
    generate_triangle_wave,
    calculate_rms_voltage,
    calculate_time_period
)


def test_sine_wave():
    assert generate_sine_wave(10, 1, 0) == pytest.approx(0)


def test_square_wave():
    assert generate_square_wave(5, 1, 0) == 5


def test_triangle_wave():
    assert generate_triangle_wave(10, 1, 0) == 10


def test_rms_voltage():
    assert calculate_rms_voltage(10) == pytest.approx(7.0710678)


def test_time_period():
    assert calculate_time_period(50) == pytest.approx(0.02)


def test_zero_frequency():
    with pytest.raises(ValueError):
        calculate_time_period(0)


def test_negative_amplitude():
    with pytest.raises(ValueError):
        generate_sine_wave(-10, 50, 0)
