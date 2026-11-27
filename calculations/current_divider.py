def calculate_current_divider(total_current, r1, r2):
    """
    Calculate current through two parallel resistors.

    I1 = Itotal * R2 / (R1 + R2)
    I2 = Itotal * R1 / (R1 + R2)
    """

    if total_current < 0:
        raise ValueError("Current cannot be negative.")

    if r1 <= 0 or r2 <= 0:
        raise ValueError("Resistances must be greater than zero.")

    current_r1 = total_current * r2 / (r1 + r2)
    current_r2 = total_current * r1 / (r1 + r2)

    return current_r1, current_r2   