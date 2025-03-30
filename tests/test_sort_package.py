from sort_function import sort_package
import pytest

# STANDARD cases
@pytest.mark.standard
@pytest.mark.parametrize("width, height, length, mass, expected", [
    (50, 50, 50, 10, "STANDARD"),
    (10, 10, 10, 1, "STANDARD"),
])
def test_standard_cases(width, height, length, mass, expected):
    assert sort_package(width, height, length, mass) == expected


# SPECIAL cases
@pytest.mark.special
@pytest.mark.parametrize("width, height, length, mass, expected", [
    (50, 50, 50, 21, "SPECIAL"),             # Only mass too heavy
    (151, 40, 40, 10, "SPECIAL"),            # Only dimension too large
    (100, 100, 100, 10, "SPECIAL"),          # Volume too large
    (40, 40, 40, 20, "SPECIAL"),             # Mass exactly at the limit
    (150, 40, 40, 10, "SPECIAL"),            # Dimension exactly at the limit
    (100, 100, 100, 10, "SPECIAL"),          # Volume exactly at the limit
])
def test_special_cases(width, height, length, mass, expected):
    assert sort_package(width, height, length, mass) == expected


# REJECTED cases
@pytest.mark.rejected
@pytest.mark.parametrize("width, height, length, mass, expected", [
    (160, 40, 40, 21, "REJECTED"),           # Mass and dimension too large
    (100, 100, 100, 25, "REJECTED"),         # Mass and volume too large
    (160, 200, 100, 30, "REJECTED"),         # All too large
    (200, 100, 100, 20, "REJECTED"),         # Volume and mass at limit
])
def test_rejected_cases(width, height, length, mass, expected):
    assert sort_package(width, height, length, mass) == expected


# INVALID INPUT cases
@pytest.mark.invalid
@pytest.mark.parametrize("width, height, length, mass, expected", [
    # Negative values
    (-10, 50, 50, 10, "INVALID INPUT"),
    (50, -10, 50, 10, "INVALID INPUT"),
    (50, 50, -10, 10, "INVALID INPUT"),
    (50, 50, 50, -10, "INVALID INPUT"),

    # Non-numeric inputs
    ('a', 50, 50, 10, "INVALID INPUT"),
    (50, 'b', 50, 10, "INVALID INPUT"),
    (50, 50, 'c', 10, "INVALID INPUT"),
    (50, 50, 50, 'mass', "INVALID INPUT"),
    (None, 50, 50, 10, "INVALID INPUT"),
])
def test_invalid_inputs(width, height, length, mass, expected):
    assert sort_package(width, height, length, mass) == expected
