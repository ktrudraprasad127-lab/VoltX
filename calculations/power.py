def calculate_power_voltage_current(voltage, current):
    if voltage < 0 or current < 0:
        raise ValueError("Values cannot be negative.")

    return voltage * current


def calculate_power_current_resistance(current, resistance):
    if current < 0 or resistance < 0:
        raise ValueError("Values cannot be negative.")

    return current ** 2 * resistance


def calculate_power_voltage_resistance(voltage, resistance):
    if voltage < 0 or resistance <= 0:
        raise ValueError("Invalid voltage or resistance.")

    return voltage ** 2 / resistance
