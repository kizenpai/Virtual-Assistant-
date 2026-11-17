"""
Unit tests for safe mathematical calculator module.
"""

import pytest
from utils.calculator import calculate, extract_math_expression

def test_extract_math_expression_natural_language():
    assert extract_math_expression("what is 5 plus 10") == "5 + 10"
    assert extract_math_expression("calculate 20 times 3") == "20 * 3"
    assert extract_math_expression("how much is 100 divided by 4") == "100 / 4"
    assert extract_math_expression("solve 2 to the power of 8") == "2 ** 8"
    assert extract_math_expression("what is 15 minus 7?") == "15 - 7"

def test_basic_addition():
    result = calculate("5 + 12")
    assert "17" in result

def test_basic_subtraction():
    result = calculate("100 - 45")
    assert "55" in result

def test_multiplication():
    result = calculate("8 * 9")
    assert "72" in result

def test_division():
    result = calculate("48 / 6")
    assert "8" in result

def test_floating_point():
    result = calculate("7 / 2")
    assert "3.5" in result

def test_power_operation():
    result = calculate("2 ** 5")
    assert "32" in result

def test_math_functions():
    result = calculate("sqrt(144)")
    assert "12" in result

def test_division_by_zero():
    result = calculate("10 / 0")
    assert "Cannot divide by zero" in result

def test_invalid_syntax():
    result = calculate("5 + + * 3")
    assert "Could not parse" in result or "error" in result.lower()

def test_empty_expression():
    result = calculate("")
    assert "Please provide a valid" in result

def test_disallowed_code_injection():
    # Verify malicious imports or arbitrary calls are blocked safely
    result = calculate("__import__('os').system('dir')")
    assert "error" in result.lower() or "not supported" in result.lower() or "undefined" in result.lower()

