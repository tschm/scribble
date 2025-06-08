"""Tests for the imports cell in app.py."""
import marimo as mo

from app import imports


def test_imports_cell():
    """Test the imports cell returns the marimo module."""
    # Call the function
    result = imports.run()

    # Check the result
    assert isinstance(result, tuple)
    assert len(result) == 2

    # The second element should be a dictionary with the marimo module
    assert "mo" in result[1]
    assert result[1]["mo"] == mo
