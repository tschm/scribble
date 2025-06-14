"""Testing the plots."""
import plotly.graph_objs as go
import pytest

from apps.app import create

"""Test suite for assessing the behavior and features of the plot creation function.

This test module is designed to validate the correctness and flexibility of the `create` function,
which is expected to generate a plotly Figure. Multiple test cases are provided to verify the
function's output under different inputs, edge cases, and expected characteristics of the returned
figure object.
"""


@pytest.mark.parametrize(
    "name, fct, event, n, test_id",
    [
        ("Thomas", "sinh(3*z)", "wedding", 100, "default"),  # Default parameters
        ("Test", "sinh(3*z)", "wedding", 100, "different_name"),  # Test with different name
        ("Thomas", "exp((-1+2j)*z)", "wedding", 100, "different_function"),  # Test with different function
        ("Thomas", "sinh(3*z)", "test", 100, "different_event"),  # Test with different event
        ("Thomas", "sinh(3*z)", "wedding", 50, "different_n"),  # Test with different n
        ("", "sinh(3*z)", "wedding", 100, "empty_name"),  # Test with empty name
    ],
    ids=lambda param: param[4] if isinstance(param, tuple) else str(param),
)
def test_create_returns_figure(name, fct, event, n, test_id):
    """Test that the create function returns a plotly Figure with various parameters."""
    fig = create(name, fct, event, n=n)
    assert isinstance(fig, go.Figure)

    # The figure should have two subplots (rows)
    assert len(fig.layout.annotations) > 0

    # The figure should have the correct background colors
    assert fig.layout.plot_bgcolor == "white"
    assert fig.layout.paper_bgcolor == "white"

    # The figure should not have a legend
    assert fig.layout.showlegend is False
