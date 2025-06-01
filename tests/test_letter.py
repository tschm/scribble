import numpy as np
import pytest


@pytest.fixture()
def letter():
    from app import _letter

    _, definitions = _letter.run()

    return definitions["letter"]


@pytest.fixture()
def letter_function():
    """
    This fixture provides the _letter function from app.py.
    """
    from app import _letter

    _, definitions = _letter.run()

    print(definitions)

    return _letter



class TestLetter:
    """Tests for the letter function in the _letter cell."""

    def test_letter_returns_array(self, letter):
        """Test that the letter function returns a numpy array."""
        result = letter("A")
        assert isinstance(result, np.ndarray)

    def test_letter_uppercase(self, letter):
        """Test that the letter function handles uppercase letters correctly."""
        result = letter("A")
        # A should have 5 points
        assert len(result) == 5
        # First point should be 0
        assert result[0] == 0
        # Second point should be 0.4+1j
        assert result[1] == 0.4 + 1j

    def test_letter_lowercase(self, letter):
        """Test that the letter function handles lowercase letters correctly."""
        # The function should convert lowercase to uppercase
        upper_result = letter("A")
        lower_result = letter("a")
        np.testing.assert_array_equal(upper_result, lower_result)

    def test_letter_space(self, letter):
        """Test that the letter function handles spaces correctly."""
        result = letter(" ")
        assert len(result) == 0

    def test_letter_invalid(self, letter):
        """Test that the letter function raises an error for invalid characters."""
        with pytest.raises(KeyError):
            letter("1")

    def test_all_letters_defined(self, letter):
        """Test that all letters A-Z and space are defined."""
        import string
        for char in string.ascii_uppercase + " ":
            result = letter(char)
            assert isinstance(result, np.ndarray)

    def test_letter_complex_values(self, letter):
        """Test that the letter function returns complex values."""
        result = letter("A")
        # Check that at least one point has a non-zero imaginary part
        assert any(point.imag != 0 for point in result if point != 0)

    def test_letter_function_return(self, letter_function):
        """Test that the _letter function is a marimo cell with the expected properties."""
        # Check that the letter_function is a marimo cell
        assert str(type(letter_function).__name__) == "Cell"

        # Check that the letter_function has the expected name
        assert letter_function._name == "_letter"

        # Check that the letter_function has the expected signature
        assert letter_function._expected_signature == ('np',)
