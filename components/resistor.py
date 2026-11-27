def calculate_resistor_power(voltage, resistance):
    """
    Calculate power dissipated by a resistor.
    P = V² / R
    """
    if voltage < 0 or resistance <= 0:
        raise ValueError("Invalid voltage or resistance.")

    return voltage ** 2 / resistance


def calculate_resistor_voltage(current, resistance):
    """
    Calculate voltage across a resistor.
    V = I * R
    """
    if current < 0 or resistance < 0:
        raise ValueError("Current and resistance cannot be negative.")

    return current * resistance


def calculate_resistor_current(voltage, resistance):
    """
    Calculate current through a resistor.
    I = V / R
    """
    if voltage < 0 or resistance <= 0:
        raise ValueError("Invalid voltage or resistance.")

    return voltage / resistance