import plotly.graph_objs as go

from pyscribble import create

name: str = "Thomas Schmelzer"
fct: str = "sinh(3*z)"
event: str = "wedding"


def test_create_returns_figure() -> None:
    """Test that the create function returns a plotly Figure."""
    fig = create(name, fct, event, n=100)
    assert isinstance(fig, go.Figure)


def test_create_with_different_parameters() -> None:
    """Test that the create function works with different parameters."""
    # Test with different name
    fig1 = create("Test", fct, event, n=100)
    assert isinstance(fig1, go.Figure)

    # Test with different function
    fig2 = create(name, "z*z", event, n=100)
    assert isinstance(fig2, go.Figure)

    # Test with different event
    fig3 = create(name, fct, "test", n=100)
    assert isinstance(fig3, go.Figure)

    # Test with different n
    fig4 = create(name, fct, event, n=50)
    assert isinstance(fig4, go.Figure)


def test_create_with_empty_name() -> None:
    """Test that the create function works with an empty name."""
    fig = create("", fct, event, n=100)
    assert isinstance(fig, go.Figure)


def test_create_with_multiple_letters() -> None:
    """Test that the create function works with multiple letters."""
    # Test with a name containing multiple valid letters
    fig = create("ABC", fct, event, n=100)
    assert isinstance(fig, go.Figure)
