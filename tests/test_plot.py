import plotly.graph_objs as go
import pytest


@pytest.fixture()
def create():
    """
    This fixture provides the create function from the _plot cell.
    """
    from app import _plot

    _, definitions = _plot.run()

    return definitions["create"]


@pytest.fixture()
def plot_function():
    """
    This fixture provides the _plot function from app.py.
    """
    from app import _plot
    return _plot


class TestPlot:
    """Tests for the create function in the _plot cell."""

    def test_create_returns_figure(self, create):
        """Test that the create function returns a plotly Figure."""
        fig = create("Thomas", "sinh(3*z)", "wedding", n=100)
        assert isinstance(fig, go.Figure)

    def test_create_with_different_parameters(self, create):
        """Test that the create function works with different parameters."""
        # Test with different name
        fig1 = create("Test", "sinh(3*z)", "wedding", n=100)
        assert isinstance(fig1, go.Figure)

        # Test with different function
        fig2 = create("Thomas", "exp((-1+2j)*z)", "wedding", n=100)
        assert isinstance(fig2, go.Figure)

        # Test with different event
        fig3 = create("Thomas", "sinh(3*z)", "test", n=100)
        assert isinstance(fig3, go.Figure)

        # Test with different n
        fig4 = create("Thomas", "sinh(3*z)", "wedding", n=50)
        assert isinstance(fig4, go.Figure)

    def test_create_with_empty_name(self, create):
        """Test that the create function works with an empty name."""
        fig = create("", "sinh(3*z)", "wedding", n=100)
        assert isinstance(fig, go.Figure)

    def test_figure_has_correct_structure(self, create):
        """Test that the figure has the correct structure."""
        fig = create("Thomas", "sinh(3*z)", "wedding", n=100)

        # The figure should have traces (at least one)
        assert len(fig.data) > 0

        # The figure should have two subplots (rows)
        assert len(fig.layout.annotations) > 0

        # The figure should have the correct background colors
        assert fig.layout.plot_bgcolor == "white"
        assert fig.layout.paper_bgcolor == "white"

        # The figure should not have a legend
        assert fig.layout.showlegend is False

    def test_plot_function_return(self, plot_function):
        """Test that the _plot function is a marimo cell with the expected properties."""
        # Check that the plot_function is a marimo cell
        assert str(type(plot_function).__name__) == "Cell"

        # Check that the plot_function has the expected name
        assert plot_function._name == "_plot"

        # Check that the plot_function has the expected signature
        assert plot_function._expected_signature == ('go', 'np', 'series', 'function_map')
