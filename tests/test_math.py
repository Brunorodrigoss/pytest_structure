import pytest

"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""


# ------------------------------------------------------------------------
# A most basic test funcion
# ------------------------------------------------------------------------
@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


# ------------------------------------------------------------------------
# A test function to show assertion instrospection
# ------------------------------------------------------------------------
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


# ------------------------------------------------------------------------
# A test function that verifies an exception
# ------------------------------------------------------------------------
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


# ------------------------------------------------------------------------
# Parametrized Tests Cases
#   Multiplication test ideas
#       - two positive integers
#       - indentity: multiplying any number by 1
#       - zero: multiplying any number by 0
#       - positive by a negative
#       - negative by a negative
#       - multiplying floats
@pytest.mark.math
def test_multiply_two_positive_ints():
    assert 2 * 3 == 6


@pytest.mark.math
def test_multiply_identity():
    assert 1 * 99 == 99


@pytest.mark.math
def test_multiply_zero():
    assert 0 * 100 == 0


# DRY Principle: Don't repeat Yoursealf!
# ------------------------------------------------------------------------

products = [
    (2, 3, 6),  # positive numbers
    (1, 99, 99),  # identity
    (0, 99, 0),  # zero
    (3, -4, -12),  # positive by negative
    (-5, -5, 25),  # negative by negative
    (2.5, 6.7, 16.75),  # floats
]


@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
