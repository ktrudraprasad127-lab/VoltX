def calculate_voltage_divider(input_voltage, r1, r2):
    """
    Calculate output voltage using:
    Vout = Vin * R2 / (R1 + R2)
    """

    if input_voltage < 0:
        raise ValueError("Input voltage cannot be negative.")

    if r1 <= 0 or r2 <= 0:
        raise ValueError("Resistances must be greater than zero.")

    return input_voltage * r2 / (r1 + r2)