import math


def calculate_inductor_energy(inductance, current):
    """
    Calculate energy stored in an inductor.
    E = 1/2 * L * I^2
    """
    if inductance <= 0 or current < 0:
        raise ValueError("Invalid inductance or current.")

    energy = 0.5 * inductance * current ** 2
    return energy


def calculate_inductive_reactance(frequency, inductance):
    """
    Calculate inductive reactance.
    XL = 2 * pi * f * L
    """
    if frequency < 0 or inductance <= 0:
        raise ValueError("Invalid frequency or inductance.")

    reactance = 2 * math.pi * frequency * inductance
    return reactance