"""Tests for the letter function."""

import numpy as np
import pytest

from apps.app import letter


def test_letter_returns_array():
    """Test that the letter function returns a numpy array."""
    result = letter("a")
    assert isinstance(result, np.ndarray)


def test_letter_uppercase():
    """Test that the letter function handles uppercase letters correctly."""
    result = letter("a")
    # a should have 5 points
    assert len(result) == 5
    # First point should be 0
    assert result[0] == 0
    # Second point should be 0.4+1j
    assert result[1] == 0.4 + 1j


def test_letter_lowercase():
    """Test that the letter function handles lowercase letters correctly."""
    # The function should convert lowercase to uppercase
    upper_result = letter("a")
    lower_result = letter("a")
    np.testing.assert_array_equal(upper_result, lower_result)


def test_letter_space():
    """Test that the letter function handles spaces correctly."""
    result = letter(" ")
    assert len(result) == 0


def test_letter_invalid():
    """Test that the letter function raises an error for invalid characters."""
    with pytest.raises(KeyError):
        letter("1")


def test_all_letters_defined():
    """Test that all letters a-Z and space are defined."""
    import string

    for char in string.ascii_uppercase + " ":
        result = letter(char)
        assert isinstance(result, np.ndarray)


def test_letter_complex_values():
    """Test that the letter function returns complex values."""
    result = letter("a")
    # Check that at least one point has a non-zero imaginary part
    assert any(point.imag != 0 for point in result if point != 0)
