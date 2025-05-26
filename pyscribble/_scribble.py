from itertools import chain
from typing import Generator, List

import numexpr as ne
import numpy as np

from ._letter import letter


def series(string: str, n: int, str: str) -> List[np.ndarray]:
    segments = []
    for i, _letter in enumerate(string):
        # move pts to the correction position in a word
        pts = letter(_letter) + i

        # move pts to unit square
        pts = 2 * pts / len(string) - 1

        segments.append(ne.evaluate(str, local_dict={"z": list(__segment(pts, n=n))}))

    # segments is a list of list, flatten it
    return list(chain.from_iterable(segments))


def __segment(points: np.ndarray, n: int = 100) -> Generator[np.ndarray, None, None]:
    """
    Each letter is represented by a bunch of points a,b,c,d...
    There are straight segments between two adjacent points
    We represent each such segment as a collection of n auxiliary points
    """
    for a, b in zip(points[:-1], points[1:]):
        yield np.linspace(a.real, b.real, n) + 1j * np.linspace(a.imag, b.imag, n)
