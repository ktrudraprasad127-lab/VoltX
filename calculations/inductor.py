import math


def calculate_inductive_reactance(frequency, inductance):
    if frequency < 0 or inductance < 0:
        raise ValueError("Values cannot be negative.")

    return 2 * math.pi * frequency * inductance


def calculate_inductor_energy(inductance, current):
    if inductance < 0 or current < 0:
        raise ValueError("Values cannot be negative.")

    return 0.5 * inductance * current ** 2
