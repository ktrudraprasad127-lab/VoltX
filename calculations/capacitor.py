
def calculate_charge(capacitance, voltage):
    """Calculate charge using Q = C * V."""

    if capacitance < 0:
        raise ValueError("Capacitance cannot be negative.")

    if voltage < 0:
        raise ValueError("Voltage cannot be negative.")

    return capacitance * voltage


def calculate_capacitance(charge, voltage):
    """Calculate capacitance using C = Q / V."""

    if voltage <= 0:
        raise ValueError("Voltage must be greater than zero.")

    if charge < 0:
        raise ValueError("Charge cannot be negative.")

    return charge / voltage
 