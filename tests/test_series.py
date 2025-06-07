import numpy as np
import pytest
from app import series



@pytest.fixture()
def fct():
    def sinh_func(z):
        """Hyperbolic sine function: sinh(3*z)"""
        return np.sinh(3*z)

    return sinh_func



class TestSeries:
    """Tests for the series function in the _series cell."""

    def test_series_returns_list(self, fct):
        """Test that the series function returns a list."""
        result = series("A", n=10, fct=fct)
        assert isinstance(result, list)

    def test_series_with_single_letter(self, fct):
        """Test the series function with a single letter."""
        result = series("A", n=10, fct=fct)
        assert len(result) > 0
        for segment in result:
            assert isinstance(segment, np.ndarray)

    def test_series_with_multiple_letters(self, fct):
        """Test the series function with multiple letters."""
        result = series("AB", n=10, fct=fct)
        assert len(result) > 0

        # Result for multiple letters should be longer than for a single letter
        single_letter_result = series("A", n=10, fct=fct)
        assert len(result) > len(single_letter_result)

    def test_series_with_function(self, fct):
        """Test the series function with a non-trivial function."""
        result = series("A", n=10, fct=lambda z: z*z)
        assert len(result) > 0

        # The function z*z should square each point
        identity_result = series("A", n=10, fct=lambda z: z)

        # The results should have the same length
        assert len(result) == len(identity_result)

        # But the points should be different
        assert any(np.any(result[i] != identity_result[i]) for i in range(len(result)))

    def test_series_with_empty_string(self, fct):
        """Test the series function with an empty string."""
        result = series("", n=10, fct=fct)
        assert isinstance(result, list)
        assert len(result) == 0
