import pytest

from calculations.inductor import (
    calculate_inductive_reactance,
    calculate_inductor_energy
)


def test_inductive_reactance():
    assert calculate_inductive_reactance(50, 0.1) == pytest.approx(31.4159, rel=1e-4)


def test_inductor_energy():
    assert calculate_inductor_energy(0.5, 2) == 1


def test_negative_frequency():
    with pytest.raises(ValueError):
        calculate_inductive_reactance(-50, 0.1)


def test_negative_current():
    with pytest.raises(ValueError):
        calculate_inductor_energy(0.5, -2)