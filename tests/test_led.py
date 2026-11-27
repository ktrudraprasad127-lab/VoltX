import pytest

from components.led import calculate_led_resistor


def test_led_resistor():
    result = calculate_led_resistor(12, 2, 0.02)

    assert result["resistance"] == 500
    assert result["power"] == pytest.approx(0.2)


def test_high_supply_voltage():
    result = calculate_led_resistor(9, 3, 0.02)

    assert result["resistance"] == 300


def test_supply_voltage_less_than_led_voltage():
    with pytest.raises(ValueError):
        calculate_led_resistor(2, 3, 0.02)


def test_zero_led_current():
    with pytest.raises(ValueError):
        calculate_led_resistor(12, 2, 0)


def test_negative_voltage():
    with pytest.raises(ValueError):
        calculate_led_resistor(-12, 2, 0.02)
