def calculate_base_current(collector_current, current_gain):
    """
    Calculate transistor base current.
    Ib = Ic / Beta
    """
    if collector_current < 0 or current_gain <= 0:
        raise ValueError("Invalid collector current or current gain.")

    return collector_current / current_gain


def calculate_collector_current(base_current, current_gain):
    """
    Calculate collector current.
    Ic = Beta * Ib
    """
    if base_current < 0 or current_gain <= 0:
        raise ValueError("Invalid base current or current gain.")

    return base_current * current_gain


def calculate_transistor_power(voltage_ce, collector_current):
    """
    Calculate transistor power dissipation.
    P = Vce * Ic
    """
    if voltage_ce < 0 or collector_current < 0:
        raise ValueError("Voltage and current cannot be negative.")

    return voltage_ce * collector_current   