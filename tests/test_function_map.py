"""Tests for the function_map function in app.py."""
import numpy as np

from app import function_map


def test_function_map_contains_expected_functions():
    """Test that the function_map contains the expected functions."""
    # Check that the function_map contains the expected keys
    assert "tanh((-1+2j)*z)" in function_map()
    assert "sinh(3*z)" in function_map()
    assert "exp((-1+2j)*z)" in function_map()

    # Check that the values are callable
    assert callable(function_map()["tanh((-1+2j)*z)"])
    assert callable(function_map()["sinh(3*z)"])
    assert callable(function_map()["exp((-1+2j)*z)"])


def test_tanh_function():
    """Test that the tanh function works correctly."""
    # Get the tanh function from the function_map
    tanh_func = function_map()["tanh((-1+2j)*z)"]

    # Test with a simple input
    z = 1.0
    result = tanh_func(z)

    # Check that the result is as expected
    expected = np.tanh((-1+2j) * z)
    np.testing.assert_allclose(result, expected)


def test_sinh_function():
    """Test that the sinh function works correctly."""
    # Get the sinh function from the function_map
    sinh_func = function_map()["sinh(3*z)"]

    # Test with a simple input
    z = 1.0
    result = sinh_func(z)

    # Check that the result is as expected
    expected = np.sinh(3 * z)
    np.testing.assert_allclose(result, expected)


def test_exp_function():
    """Test that the exp function works correctly."""
    # Get the exp function from the function_map
    exp_func = function_map()["exp((-1+2j)*z)"]

    # Test with a simple input
    z = 1.0
    result = exp_func(z)

    # Check that the result is as expected
    expected = np.exp((-1+2j) * z)
    np.testing.assert_allclose(result, expected)
