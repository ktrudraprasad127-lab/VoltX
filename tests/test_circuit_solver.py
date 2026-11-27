import pytest

from circuit_analysis.circuit_solver import (
    solve_series_circuit,
    solve_parallel_circuit
)


def test_series_circuit():
    result = solve_series_circuit(12, [10, 20])

    assert result["total_resistance"] == 30
    assert result["total_current"] == pytest.approx(0.4)
    assert result["voltage_drops"] == pytest.approx([4, 8])


def test_parallel_circuit():
    result = solve_parallel_circuit(12, [10, 20])

    assert result["total_resistance"] == pytest.approx(6.6666667)
    assert result["total_current"] == pytest.approx(1.8)
    assert result["branch_currents"] == pytest.approx([1.2, 0.6])


def test_empty_resistance_list():
    with pytest.raises(ValueError):
        solve_series_circuit(12, [])


def test_zero_resistance():
    with pytest.raises(ValueError):
        solve_parallel_circuit(12, [10, 0])


def test_negative_voltage():
    with pytest.raises(ValueError):
        solve_series_circuit(-12, [10, 20])
