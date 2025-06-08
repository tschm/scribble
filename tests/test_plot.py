"""Testing the plots."""
import plotly.graph_objs as go

from app import create

"""Test suite for assessing the behavior and features of the plot creation function.

This test module is designed to validate the correctness and flexibility of the `create` function,
which is expected to generate a plotly Figure. Multiple test cases are provided to verify the
function's output under different inputs, edge cases, and expected characteristics of the returned
figure object.
"""


def test_create_returns_figure():
    """Test that the create function returns a plotly Figure."""
    fig = create(name="Thomas", fct="sinh(3*z)", event="wedding", n=100)
    assert isinstance(fig, go.Figure)


def test_create_with_different_parameters():
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


def test_create_with_empty_name():
    """Test that the create function works with an empty name."""
    fig = create("", "sinh(3*z)", "wedding", n=100)
    assert isinstance(fig, go.Figure)


def test_figure_has_correct_structure():
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
