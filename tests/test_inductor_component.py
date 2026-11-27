import pytest

from components.inductor import (
    calculate_inductor_energy,
    calculate_inductive_reactance
)


def test_inductor_energy():
    assert calculate_inductor_energy(0.5, 2) == pytest.approx(1.0)


def test_zero_current_energy():
    assert calculate_inductor_energy(0.5, 0) == 0


def test_invalid_inductance():
    with pytest.raises(ValueError):
        calculate_inductor_energy(0, 2)


def test_inductive_reactance():
    assert calculate_inductive_reactance(50, 0.1) == pytest.approx(31.4159)


def test_zero_frequency():
    assert calculate_inductive_reactance(0, 0.1) == 0


def test_negative_frequency():
    with pytest.raises(ValueError):
        calculate_inductive_reactance(-50, 0.1)


def test_negative_inductance():
    with pytest.raises(ValueError):
        calculate_inductive_reactance(50, -0.1)
