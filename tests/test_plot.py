from pyscribble import create

name: str = "Thomas Schmelzer"
fct: str = "sinh(3*z)"
event: str = "wedding"


def test_plot() -> None:
    fig = create(name, fct, event, n=100)
    # Show the figure
    fig.show()
