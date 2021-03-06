from math_series.series import fibonacci, lucas, sum_series
import pytest

# test fibonacci function with valid input
def test_fibonacci_with_valid_input_0():
    assert fibonacci(0) == 0

def test_fibonacci_with_valid_input_1():
    assert fibonacci(1) == 1

def test_fibonacci_with_valid_input_2():
    assert fibonacci(2) == 1

def test_fibonacci_with_valid_input_3():
    assert fibonacci(3) == 2

def test_fibonacci_with_valid_input_4():
    assert fibonacci(4) == 3

# test fibonacci function with invalid input
def test_fibonacci_with_invalid_input_negative_integer():
    assert fibonacci(-1) == None

def test_fibonacci_with_invalid_input_float():
    assert fibonacci(3.14) == None

def test_fibonacci_with_invalid_input_string():
    assert fibonacci("hello") == None

# test lucas function with valid input
def test_lucas_with_valid_input_0():
    assert lucas(0) == 2

def test_lucas_with_valid_input_1():
    assert lucas(1) == 1

def test_lucas_with_valid_input_2():
    assert lucas(2) == 3

def test_lucas_with_valid_input_3():
    assert lucas(3) == 4

def test_lucas_with_valid_input_4():
    assert lucas(4) == 7

# test lucas function with invalid input
def test_lucas_with_invalid_input_negative_number():
    assert lucas(-10) == None

def test_lucas_with_invalid_input_float():
    assert lucas(2.5) == None

def test_lucas_with_invalid_input_string():
    assert lucas("world") == None

# test sum_series function with valid input
def test_sum_series_with_valid_input_and_default_arguments():
    assert sum_series(5) == 5

def test_sum_series_with_valid_input_5_2_1():
    assert sum_series(5, 2, 1) == 11

def test_sum_series_with_valid_input_5_2_2():
    assert sum_series(5, 2, 2) == 16

# test sum_series function with invalid input
def test_sum_series_with_invalid_input_hello_1_5():
    assert sum_series("hello", 1, 5) == None
