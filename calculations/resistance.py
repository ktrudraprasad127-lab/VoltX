
COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

MULTIPLIERS = {
    "black": 1,
    "brown": 10,
    "red": 100,
    "orange": 1000,
    "yellow": 10000,
    "green": 100000,
    "blue": 1000000,
    "gold": 0.1,
    "silver": 0.01
}

TOLERANCES = {
    "brown": 1,
    "red": 2,
    "green": 0.5,
    "blue": 0.25,
    "violet": 0.1,
    "grey": 0.05,
    "gold": 5,
    "silver": 10
}


def calculate_resistance(band1, band2, band3, band4):

    band1 = band1.lower()
    band2 = band2.lower()
    band3 = band3.lower()
    band4 = band4.lower()

    if band1 not in COLOR_CODES:
        raise ValueError("Invalid first band color")

    if band2 not in COLOR_CODES:
        raise ValueError("Invalid second band color")

    if band3 not in MULTIPLIERS:
        raise ValueError("Invalid multiplier color")

    if band4 not in TOLERANCES:
        raise ValueError("Invalid tolerance color")

    first_digit = COLOR_CODES[band1]
    second_digit = COLOR_CODES[band2]

    multiplier = MULTIPLIERS[band3]
    tolerance = TOLERANCES[band4]

    resistance = (
        first_digit * 10 + second_digit
    ) * multiplier

    return resistance, tolerance
