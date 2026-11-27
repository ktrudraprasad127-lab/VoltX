def calculate_energy_joules(power, time_seconds):
    """
    Calculate energy in Joules.
    E = P * t
    """

    if power < 0 or time_seconds < 0:
        raise ValueError("Values cannot be negative.")

    return power * time_seconds


def calculate_energy_kwh(power_watts, time_hours):
    """
    Calculate energy consumption in kWh.
    Energy = Power(W) * Time(hours) / 1000
    """

    if power_watts < 0 or time_hours < 0:
        raise ValueError("Values cannot be negative.")

    return (power_watts * time_hours) / 1000