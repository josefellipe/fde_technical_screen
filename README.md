# Package Sorter

This project provides a Python function to classify packages based on their dimensions and weight. It also includes a complete test suite using `pytest`.

---

## Function Overview

The main function is:

sort_package(width, height, length, mass)
It returns a classification string based on the following rules:

STANDARD: All values are within the allowed limits.
SPECIAL: Only one of the rules is exceeded (dimension ≥ 150 cm, volume ≥ 1,000,000 cm³, or mass ≥ 20 kg).
REJECTED: The mass is too heavy (≥ 20 kg) and at least one other limit is also exceeded.
INVALID INPUT: One or more inputs are non-numeric or negative.

# How to Use
1. Clone the repository
git clone https://github.com/josefellipe/fde_technical_screen
cd fde_technical_screen

2. Create and activate a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows

3. Install dependencies
pip install -r requirements.txt

# Running the Tests
Tests are written using pytest and organized into four categories:

standard
special
rejected
invalid

Run all tests
pytest -v

Run a specific group of tests
pytest -v -m special

Custom markers are defined in pytest.ini.

📁 Project Structure

package-sorter/
├── sort_function.py           # Main function logic
├── tests/
│   └── test_sort_package.py   # Full test suite using pytest
├── pytest.ini                 # Declares custom test markers
└── requirements.txt           # List of required dependencies
