"""Test suite for assessing the behavior and features of the plot creation function.

This test module is designed to validate the correctness and flexibility of the `create` function,
which is expected to generate a plotly Figure. Multiple test cases are provided to verify the
function's output under different inputs, edge cases, and expected characteristics of the returned
figure object.
"""

import plotly.graph_objs as go
import pytest

from apps.app import create


@pytest.mark.parametrize(
    ("name", "fct", "event", "n"),
    [
        ("Thomas", "sinh(3*z)", "wedding", 100),
        ("Test", "sinh(3*z)", "wedding", 100),
        ("Thomas", "exp((-1+2j)*z)", "wedding", 100),
        ("Thomas", "sinh(3*z)", "test", 100),
        ("Thomas", "sinh(3*z)", "wedding", 50),
        ("", "sinh(3*z)", "wedding", 100),
    ],
)
def test_create_returns_figure(name, fct, event, n):
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
