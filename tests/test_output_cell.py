"""Tests for the __output cell in app.py."""
from unittest.mock import MagicMock

import marimo as mo

from app import __output


def test_output_cell():
    """Test the __output cell by mocking dropdown, event, and name."""
    # Create mocks for mo, dropdown, event, and name
    mock_dropdown = MagicMock()
    mock_event = MagicMock()
    mock_name = MagicMock()

    # Set up the values for the mocks
    mock_dropdown.value = "sinh(3*z)"
    mock_event.value = "Test Event"
    mock_name.value = "Test Name"

    result = __output.run(mo=mo, dropdown=mock_dropdown, event=mock_event, name=mock_name)

    # Check the result
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert "fig" in result[1].keys()
    assert "buf" in result[1].keys()
