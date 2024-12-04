import numexpr as ne
import numpy as np

from .letter import letter

# def segment(points, n=100):
#     """
#     Each letter is a represented by a bunch of points a,b,c,d...
#     There are straight segments between two adjacent points
#     We represent each such segment as a collection of n auxilliary points
#     """
#     for a, b in zip(points[:-1], points[1:]):
#         yield np.linspace(a.real, b.real, n) + 1j * np.linspace(a.imag, b.imag, n)
#
#
# def scribble(axes, text, f, title="", **kwargs):
#     axes.set_axis_off()
#
#     for n, _letter in enumerate(text):
#         # move a letter into the complex plane
#         points = letter(_letter) + n
#
#         # move the points to the unit-square
#         points = 2 * points / len(text) - 1
#
#         # each segment is a straight line of n points
#         for z in segment(points, n=100):
#             t = ne.evaluate(f)
#             # plot the name in the complex plane
#             axes.plot(t.real, t.imag, **kwargs)
#
#     axes.set_title(title)
#
#
# def wedding(word, f, title):
#     fig, axes = plt.subplots(
#         nrows=2, ncols=1, figsize=(8.27, 11.69), subplot_kw={"aspect": "equal"}
#     )
#
#     scribble(axes[1], text=word, f=f, title=title, linewidth=2, color="blue")
#
#     axes[0].set_axis_off()
#     axes[0].text(
#         0.5,
#         0.5,
#         "{name}\n{function}".format(name=word, function=f),
#         horizontalalignment="right",
#         rotation=180,
#     )
#
#     return fig


def series(string, n, str="sinh(3*z)"):
    for i, _letter in enumerate(string):
        # move pts to the correction position in a word
        pts = letter(_letter) + i

        # move pts to unit square
        pts = 2 * pts / len(string) - 1

        list(__segment(pts, n=n))

        yield _letter, ne.evaluate(str)


def __segment(points, n=100):
    """
    Each letter is a represented by a bunch of points a,b,c,d...
    There are straight segments between two adjacent points
    We represent each such segment as a collection of n auxilliary points
    """
    for a, b in zip(points[:-1], points[1:]):
        yield np.linspace(a.real, b.real, n) + 1j * np.linspace(a.imag, b.imag, n)
