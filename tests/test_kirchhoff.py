import pytest

from circuit_analysis.kirchhoff import (
    calculate_kcl,
    calculate_kvl
)


def test_kcl_balanced():
    result = calculate_kcl([5, 3], [4, 4])
    assert result["incoming_current"] == 8
    assert result["outgoing_current"] == 8
    assert result["balanced"] is True


def test_kcl_unbalanced():
    result = calculate_kcl([5, 3], [4, 2])
    assert result["balanced"] is False


def test_kvl_balanced():
    result = calculate_kvl([12], [5, 7])
    assert result["balanced"] is True


def test_kvl_unbalanced():
    result = calculate_kvl([12], [5, 6])
    assert result["balanced"] is False


def test_negative_current():
    with pytest.raises(ValueError):
        calculate_kcl([-5], [5])
