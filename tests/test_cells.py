from unittest.mock import MagicMock

import numpy as np
import plotly.graph_objs as go


class TestCells:
    """Tests for the cell functions in app.py."""

    def test_letter_cell(self):
        """Test that the _letter cell returns the expected definitions."""
        from app import _letter

        # Create a mock np module
        np_mock = MagicMock()
        np_mock.array = MagicMock(return_value=np.array([]))
        np_mock.ndarray = np.ndarray

        # Run the cell with the mock np module
        result, definitions = _letter.run(np=np_mock)

        # Check that the definitions contain the letter function
        assert "letter" in definitions
        assert callable(definitions["letter"])

        # Check that the result is a tuple with the letter function
        #assert isinstance(result, tuple)
        #assert len(result) == 1
        #assert result[0] == definitions["letter"]

    def test_series_cell(self):
        """Test that the _series cell returns the expected definitions."""
        from app import _series

        # Create mock objects for the letter and np parameters
        letter_mock = MagicMock()
        np_mock = MagicMock()
        np_mock.ndarray = np.ndarray

        # Run the cell with the mock parameters
        result, definitions = _series.run(letter=letter_mock, np=np_mock)

        # Check that the definitions contain the series function
        assert "series" in definitions
        assert callable(definitions["series"])

        # Check that the result is a tuple with the series function
        #assert isinstance(result, tuple)
        #assert len(result) == 1
        #assert result[0] == definitions["series"]

    def test_plot_cell(self):
        """Test that the _plot cell returns the expected definitions."""
        from app import _plot

        # Create mock objects for the go, np, and series parameters
        go_mock = MagicMock()
        go_mock.Figure = go.Figure
        go_mock.Scatter = go.Scatter
        np_mock = MagicMock()
        series_mock = MagicMock()

        # Run the cell with the mock parameters
        result, definitions = _plot.run(go=go_mock, np=np_mock, series=series_mock)

        # Check that the definitions contain the create function
        assert "create" in definitions
        assert callable(definitions["create"])

        # Check that the result is a tuple with the create function
        #assert isinstance(result, tuple)
        #assert len(result) == 1
        #assert result[0] == definitions["create"]

    def test_input_name_cell(self):
        """Test that the __input_name cell returns the expected definitions."""
        import app

        # Create a mock mo module
        mo_mock = MagicMock()
        name_mock = MagicMock()
        mo_mock.ui.text.return_value = name_mock
        mo_mock.md.return_value = None

        # Get the cell function by name
        input_name_cell = getattr(app, "__input_name")

        # Run the cell with the mock mo module
        _, definitions = input_name_cell.run(mo=mo_mock)

        # Check that the definitions contain the name input
        assert "name" in definitions
        assert definitions["name"] == name_mock

    def test_input_event_cell(self):
        """Test that the __input_event cell returns the expected definitions."""
        import app

        # Create a mock mo module
        mo_mock = MagicMock()
        event_mock = MagicMock()
        mo_mock.ui.text.return_value = event_mock
        mo_mock.md.return_value = None

        # Get the cell function by name
        input_event_cell = getattr(app, "__input_event")

        # Run the cell with the mock mo module
        _, definitions = input_event_cell.run(mo=mo_mock)

        # Check that the definitions contain the event input
        assert "event" in definitions
        assert definitions["event"] == event_mock
