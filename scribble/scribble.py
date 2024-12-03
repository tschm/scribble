import numexpr as ne
import numpy as np

from scribble.letter import letter


def __segment(points, n=100):
    """
    Each letter is a represented by a bunch of points a,b,c,d...
    There are straight segments between two adjacent points
    We represent each such segment as a collection of n auxilliary points
    """
    for a, b in zip(points[:-1], points[1:]):
        yield np.linspace(a.real, b.real, n) + 1j * np.linspace(a.imag, b.imag, n)


def scribble(axes, text, f, title="Lydia & Thomas, August 17, Rhodes House", **kwargs):
    axes.set_axis_off()

    for n, _letter in enumerate(text):
        # move a letter into the complex plane
        points = letter(_letter) + n

        # move the points to the unit-square
        points = 2 * points / len(text) - 1

        # each segment is a straight line of n points
        for z in __segment(points, n=100):
            t = ne.evaluate(f)
            # plot the name in the complex plane
            axes.plot(t.real, t.imag, **kwargs)

    axes.set_title(title)
