
def solve_series_circuit(voltage, resistances):
    if voltage < 0:
        raise ValueError("Voltage cannot be negative.")

    if not resistances or any(r <= 0 for r in resistances):
        raise ValueError("All resistances must be positive.")

    total_resistance = sum(resistances)
    total_current = voltage / total_resistance

    voltage_drops = [
        total_current * resistance
        for resistance in resistances
    ]

    return {
        "total_resistance": total_resistance,
        "total_current": total_current,
        "voltage_drops": voltage_drops
    }


def solve_parallel_circuit(voltage, resistances):
    if voltage < 0:
        raise ValueError("Voltage cannot be negative.")

    if not resistances or any(r <= 0 for r in resistances):
        raise ValueError("All resistances must be positive.")

    total_resistance = 1 / sum(
        1 / resistance for resistance in resistances
    )

    total_current = voltage / total_resistance

    branch_currents = [
        voltage / resistance
        for resistance in resistances
    ]

    return {
        "total_resistance": total_resistance,
        "total_current": total_current,
        "branch_currents": branch_currents
    }
