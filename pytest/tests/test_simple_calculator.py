import pytest
import simple_calculator as calculator


def test_addition():
    assert calculator.add(20, 30) == 50


def test_addition_negative():
    assert calculator.add(-5, 3) == -2


def test_subtraction():
    assert calculator.subtract(10, 4) == 6


def test_subtraction_negative_result():
    assert calculator.subtract(4, 10) == -6


def test_multiplication():
    assert calculator.multiply(6, 7) == 42


def test_multiplication_by_zero():
    assert calculator.multiply(5, 0) == 0


def test_division():
    assert calculator.divide(10, 2) == 5


def test_division_decimal_result():
    assert calculator.divide(7, 2) == 3.5


def test_division_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(5, 0)