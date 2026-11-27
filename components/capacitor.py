import math


def calculate_capacitor_energy(capacitance, voltage):
    """
    Calculate energy stored in a capacitor.
    E = 1/2 * C * V^2
    """
    if capacitance <= 0 or voltage < 0:
        raise ValueError("Invalid capacitance or voltage.")

    energy = 0.5 * capacitance * voltage ** 2
    return energy


def calculate_capacitive_reactance(frequency, capacitance):
    """
    Calculate capacitive reactance.
    Xc = 1 / (2 * pi * f * C)
    """
    if frequency <= 0 or capacitance <= 0:
        raise ValueError("Frequency and capacitance must be positive.")

    reactance = 1 / (2 * math.pi * frequency * capacitance)
    return reactance