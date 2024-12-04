from pyscribble.plot import create

name = "Thomas"
fct = "sinh(3*z)"


def test_plot():
    fig = create(name, fct, n=100)
    # Show the figure
    fig.show()
