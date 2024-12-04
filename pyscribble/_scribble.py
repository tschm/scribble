from itertools import chain

import numexpr as ne
import numpy as np

from ._letter import letter


def series(string, n, str):
    segments = []
    for i, _letter in enumerate(string):
        # move pts to the correction position in a word
        pts = letter(_letter) + i

        # move pts to unit square
        pts = 2 * pts / len(string) - 1

        segments.append(ne.evaluate(str, local_dict={"z": list(__segment(pts, n=n))}))

    # segments is a list of list, flatten it
    return list(chain.from_iterable(segments))


def __segment(points, n=100):
    """
    Each letter is a represented by a bunch of points a,b,c,d...
    There are straight segments between two adjacent points
    We represent each such segment as a collection of n auxilliary points
    """
    for a, b in zip(points[:-1], points[1:]):
        yield np.linspace(a.real, b.real, n) + 1j * np.linspace(a.imag, b.imag, n)
