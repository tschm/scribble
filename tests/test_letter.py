import numpy as np
import pytest

from pyscribble._letter import letter


def test_letter_returns_array():
    """Test that the letter function returns a numpy array."""
    result = letter("A")
    assert isinstance(result, np.ndarray)

def test_letter_uppercase():
    """Test that the letter function handles uppercase letters correctly."""
    result = letter("A")
    # A should have 5 points
    assert len(result) == 5
    # First point should be 0
    assert result[0] == 0
    # Second point should be 0.4+1j
    assert result[1] == 0.4 + 1j

def test_letter_lowercase():
    """Test that the letter function handles lowercase letters correctly."""
    # The function should convert lowercase to uppercase
    upper_result = letter("A")
    lower_result = letter("a")
    np.testing.assert_array_equal(upper_result, lower_result)

def test_letter_space():
    """Test that the letter function handles spaces correctly."""
    result = letter(" ")
    assert len(result) == 0

def test_letter_invalid():
    """Test that the letter function raises an error for invalid characters."""
    with pytest.raises(KeyError):
        letter("1")  # Numbers are not defined in the __letters dictionary
