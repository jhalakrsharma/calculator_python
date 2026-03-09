"""Unit tests for calc_backend.py using pytest."""

import pytest
from calc_backend import square_root, add_number, subtract_number, divide_number


class TestSquareRoot:
    """Test cases for the square_root function."""

    def test_square_root_positive_number(self):
        """Test square root of positive numbers."""
        assert square_root(4) == 2.0
        assert square_root(9) == 3.0
        assert square_root(16) == 4.0

    def test_square_root_zero(self):
        """Test square root of zero."""
        assert square_root(0) == 0.0

    def test_square_root_decimal(self):
        """Test square root of decimal numbers."""
        assert square_root(2.25) == 1.5
        assert abs(square_root(2) - 1.414213562) < 1e-6

    def test_square_root_negative_number(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
            square_root(-1)
        with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
            square_root(-10)


class TestAddNumber:
    """Test cases for the add_number function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add_number(2, 3) == 5
        assert add_number(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add_number(-2, -3) == -5
        assert add_number(-10, 5) == -5

    def test_add_decimal_numbers(self):
        """Test adding decimal numbers."""
        assert add_number(1.5, 2.5) == 4.0
        assert add_number(0.1, 0.2) == pytest.approx(0.3)

    def test_add_zero(self):
        """Test adding zero."""
        assert add_number(0, 5) == 5
        assert add_number(5, 0) == 5
        assert add_number(0, 0) == 0


class TestSubtractNumber:
    """Test cases for the subtract_number function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract_number(5, 3) == 2
        assert subtract_number(10, 7) == 3

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract_number(-2, -3) == 1
        assert subtract_number(-5, 3) == -8

    def test_subtract_decimal_numbers(self):
        """Test subtracting decimal numbers."""
        assert subtract_number(5.5, 2.5) == 3.0
        assert subtract_number(0.3, 0.1) == pytest.approx(0.2)

    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract_number(5, 0) == 5
        assert subtract_number(0, 5) == -5
        assert subtract_number(0, 0) == 0


class TestDivideNumber:
    """Test cases for the divide_number function."""

    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide_number(10, 2) == 5.0
        assert divide_number(15, 3) == 5.0

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide_number(-10, 2) == -5.0
        assert divide_number(-10, -2) == 5.0

    def test_divide_decimal_numbers(self):
        """Test dividing decimal numbers."""
        assert divide_number(5.0, 2.0) == 2.5
        assert divide_number(7.5, 2.5) == 3.0

    def test_divide_zero_denominator(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide_number(10, 0)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide_number(0, 0)

    def test_divide_by_one(self):
        """Test dividing by one."""
        assert divide_number(5, 1) == 5.0
        assert divide_number(-3, 1) == -3.0
