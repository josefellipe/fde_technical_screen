from typing import Literal

PackageOpt = Literal["STANDARD", "SPECIAL", "REJECTED", "INVALID INPUT"]

def sort_package(width:float, height:float, length:float, mass:float) -> PackageOpt:
    """
    Classifies a package based on its dimensions and mass.

    - STANDARD: All within limits.
    - SPECIAL: One limit exceeded (mass ≥ 20kg, dimension ≥ 150cm, or volume ≥ 1,000,000 cm³).
    - REJECTED: Mass ≥ 20kg AND (dimension or volume limit exceeded).
    - INVALID INPUT: Non-numeric or negative input values.

    Parameters:
        width (float): Width in cm.
        height (float): Height in cm.
        length (float): Length in cm.
        mass (float): Mass in kg.

    Returns:
        str: "STANDARD", "SPECIAL", "REJECTED", or "INVALID INPUT".
    """
    MAX_DIMENSION = 150
    MAX_VOLUME = 1_000_000
    MAX_MASS = 20

    validated = validate_inputs(width, height, length, mass)
    if validated is None:
        return "INVALID INPUT"

    dimension_too_large = False
    volume_too_large = False
    mass_too_heavy = False

    if max(width, height, length) >= MAX_DIMENSION:
        dimension_too_large = True
    if width * height * length >= MAX_VOLUME:
        volume_too_large = True
    if mass >= MAX_MASS:
        mass_too_heavy = True


    if mass_too_heavy and (dimension_too_large or volume_too_large):
        return "REJECTED"
    elif mass_too_heavy or dimension_too_large or volume_too_large:
        return "SPECIAL"
    else:
        return "STANDARD"


def validate_inputs(*values):
    try:
        floats = [float(v) for v in values]
        if any(v < 0 for v in floats):
            return None
        return floats
    except (ValueError, TypeError):
        return None
