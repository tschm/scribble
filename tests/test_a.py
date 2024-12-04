from pyscribble.plot import create

name = "Thomas Schmelzer"
fct = "sinh(3*z)"
event = "wedding"


def test_plot():
    fig = create(name, fct, event, n=100)
    # Show the figure
    fig.show()
