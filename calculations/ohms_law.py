
def calculate_voltage(current, resistance):
    """Calculate voltage using V = I * R."""

    if resistance < 0 or current < 0:
        raise ValueError("Current and resistance cannot be negative.")

    voltage = current * resistance
    return voltage


def calculate_current(voltage, resistance):
    """Calculate current using I = V / R."""

    if resistance <= 0:
        raise ValueError("Resistance must be greater than zero.")

    current = voltage / resistance
    return current


def calculate_resistance(voltage, current):
    """Calculate resistance using R = V / I."""

    if current == 0:
        raise ValueError("Current cannot be zero.")

    resistance = voltage / current
    return resistance
