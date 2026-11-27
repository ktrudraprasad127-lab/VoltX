def calculate_kcl(incoming_currents, outgoing_currents):
    """
    Verify Kirchhoff's Current Law.
    Sum of incoming currents = Sum of outgoing currents.
    """

    if any(current < 0 for current in incoming_currents + outgoing_currents):
        raise ValueError("Current cannot be negative.")

    incoming = sum(incoming_currents)
    outgoing = sum(outgoing_currents)

    difference = incoming - outgoing

    return {
        "incoming_current": incoming,
        "outgoing_current": outgoing,
        "difference": difference,
        "balanced": abs(difference) < 1e-9
    }


def calculate_kvl(voltage_rises, voltage_drops):
    """
    Verify Kirchhoff's Voltage Law.
    Sum of voltage rises = Sum of voltage drops.
    """

    rises = sum(voltage_rises)
    drops = sum(voltage_drops)

    difference = rises - drops

    return {
        "voltage_rises": rises,
        "voltage_drops": drops,
        "difference": difference,
        "balanced": abs(difference) < 1e-9
    }