import numpy as np
import pytest


@pytest.fixture()
def series():
    from app import _series

    _, definitions = _series.run()

    return definitions["series"]


class TestSeries:
    """Tests for the series function in the _series cell."""

    def test_series_returns_list(self, series):
        """Test that the series function returns a list."""
        result = series("A", n=10, str="z")
        assert isinstance(result, list)

    def test_series_with_single_letter(self, series):
        """Test the series function with a single letter."""
        result = series("A", n=10, str="z")
        assert len(result) > 0
        for segment in result:
            assert isinstance(segment, np.ndarray)

    def test_series_with_multiple_letters(self, series):
        """Test the series function with multiple letters."""
        result = series("AB", n=10, str="z")
        assert len(result) > 0

        # Result for multiple letters should be longer than for a single letter
        single_letter_result = series("A", n=10, str="z")
        assert len(result) > len(single_letter_result)

    def test_series_with_function(self, series):
        """Test the series function with a non-trivial function."""
        result = series("A", n=10, str="z*z")
        assert len(result) > 0

        # The function z*z should square each point
        identity_result = series("A", n=10, str="z")

        # The results should have the same length
        assert len(result) == len(identity_result)

        # But the points should be different
        assert any(np.any(result[i] != identity_result[i]) for i in range(len(result)))

    def test_series_with_empty_string(self, series):
        """Test the series function with an empty string."""
        result = series("", n=10, str="z")
        assert isinstance(result, list)
        assert len(result) == 0
