"""Backend math operations for the calculator app."""


def square_root(number: float) -> float:
    """Return the square root of a non-negative number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return number ** 0.5


def add_number(num1: float, num2: float) -> float:
    """Return the sum of two numbers."""
    return num1 + num2


def subtract_number(num1: float, num2: float) -> float:
    """Return the difference of two numbers."""
    return num1 - num2


def divide_number(num1: float, num2: float) -> float:
    """Return the division result of num1 by num2."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2
