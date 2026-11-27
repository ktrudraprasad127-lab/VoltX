def calculate_led_resistor(supply_voltage, led_voltage, led_current):
    """
    Calculate the series resistor for an LED.

    R = (Vs - Vf) / I
    """

    if supply_voltage <= 0 or led_voltage < 0:
        raise ValueError("Invalid voltage values.")

    if led_current <= 0:
        raise ValueError("LED current must be greater than zero.")

    if supply_voltage <= led_voltage:
        raise ValueError("Supply voltage must exceed LED voltage.")

    resistance = (supply_voltage - led_voltage) / led_current

    power = led_current ** 2 * resistance

    return {
        "resistance": resistance,
        "power": power
    }