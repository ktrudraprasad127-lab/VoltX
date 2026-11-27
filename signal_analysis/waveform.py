import math


def generate_sine_wave(amplitude, frequency, time):
    """Calculate sine-wave voltage at a given time."""

    if amplitude < 0 or frequency < 0 or time < 0:
        raise ValueError("Values cannot be negative.")

    return amplitude * math.sin(2 * math.pi * frequency * time)


def generate_square_wave(amplitude, frequency, time):
    """Calculate an ideal square-wave voltage."""

    if amplitude < 0 or frequency <= 0 or time < 0:
        raise ValueError("Invalid input values.")

    angle = math.sin(2 * math.pi * frequency * time)

    return amplitude if angle >= 0 else -amplitude


def generate_triangle_wave(amplitude, frequency, time):
    """Calculate an ideal triangle-wave voltage."""

    if amplitude < 0 or frequency <= 0 or time < 0:
        raise ValueError("Invalid input values.")

    phase = (frequency * time) % 1

    return amplitude * (4 * abs(phase - 0.5) - 1)


def calculate_rms_voltage(peak_voltage):
    """Calculate RMS voltage for a sine wave."""

    if peak_voltage < 0:
        raise ValueError("Voltage cannot be negative.")

    return peak_voltage / math.sqrt(2)


def calculate_time_period(frequency):
    """Calculate time period T = 1/f."""

    if frequency <= 0:
        raise ValueError("Frequency must be greater than zero.")

    return 1 / frequency    