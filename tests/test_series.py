import pytest
from math_series.series import fibonacci
from math_series.series import lucas

#order of imports: from package_name.module_name import function_name

def test_fibonacci_exists():
    assert fibonacci

def test_fibonacci_3():
    actual = fibonacci(3)
    expected =2
    assert actual == expected

def test_fibonacci_5():
    actual = fibonacci(5)
    expected =5
    assert actual == expected

def test_fibonacci_10():
    actual = fibonacci(10)
    expected =55
    assert actual == expected

def test_fibonacci_15():
    actual = fibonacci(15)
    expected = 610
    assert actual == expected

def test_fibonacci_negative():
    actual = fibonacci(-1)
    expected = None
    assert actual == expected, f"Fibonacci of a negative number should return {expected}, but got {actual} instead."

def test_lucas_exists():
    assert lucas

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected