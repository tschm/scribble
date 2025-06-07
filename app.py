# content of test_notebook.py

import marimo

__generated_with = "0.13.15"
app = marimo.App()

with app.setup:
    import numpy as np
    import plotly.graph_objs as go


@app.cell
def imports():
    import marimo as mo
    return (mo,)


@app.function
def tanh_func(z):
    """Hyperbolic tangent function: tanh((-1+2j)*z)"""
    return np.tanh((-1+2j)*z)


@app.function
def sinh_func(z):
    """Hyperbolic sine function: sinh(3*z)"""
    return np.sinh(3*z)


@app.function
def exp_func(z):
    """Exponential function: exp((-1+2j)*z)"""
    return np.exp((-1+2j)*z)


@app.function
def function_map():
    # Map function names to actual functions
    function_map = {
        "tanh((-1+2j)*z)": tanh_func,
        "sinh(3*z)": sinh_func,
        "exp((-1+2j)*z)": exp_func,
        "custom": lambda z: np.exp((-1+2j)*4*z)
    }

    return function_map


@app.function
def create_download_link(data: str, filename: str, mime: str = "text/plain"):
    """
    Create a download link for Marimo notebooks (works in WASM).

    Args:
        data: The string content to download.
        filename: The name of the downloaded file.
        mime: The MIME type of the file (default is "text/plain").

    Returns:
        mo.md object with a download anchor tag.
    """
    import base64

    b64 = base64.b64encode(data.encode()).decode()
    href = f'data:{mime};base64,{b64}'
    html = f'<a download="{filename}" href="{href}" target="_blank">📥 Download {filename}</a>'
    return html


@app.function
def letter(x: str) -> np.ndarray:
    # I have copied this data straight from
    # https://github.com/asgeirbirkis/chebfun/blob/master/scribble.m
    __letters = {
        "A": [0, 0.4 + 1j, 0.8, 0.6 + 0.5j, 0.2 + 0.5j],
        "B": [0, 1j, 0.8 + 0.9j, 0.8 + 0.6j, 0.5j, 0.8 + 0.4j, 0.8 + 0.1j, 0],
        "C": [0.8 + 1j, 0.8j, 0.2j, 0.8],
        "D": [0, 0.8 + 0.1j, 0.8 + 0.9j, 1j, 0],
        "E": [0.8 + 1j, 1j, 0.5j, 0.5j + 0.7, 0.5j, 0, 0.8],
        "F": [0.8 + 1j, 1j, 0.5j, 0.5j + 0.7, 0.5j, 0],
        "G": [0.8 + 1j, 0.8j, 0.2j, 0.6, 0.6 + 0.5j, 0.4 + 0.5j, 0.8 + 0.5j],
        "H": [0, 1j, 0.5j, 0.5j + 0.8, 0.8 + 1j, 0.8],
        "I": [0, 0.8, 0.4, 0.4 + 1j, 1j, 0.8 + 1j],
        "J": [0, 0.4, 0.4 + 1j, 1j, 0.8 + 1j],
        "K": [0, 1j, 0.5j, 0.8 + 1j, 0.5j, 0.8],
        "L": [1j, 0, 0.8],
        "M": [0, 0.1 + 1j, 0.4, 0.7 + 1j, 0.8],
        "N": [0, 1j, 0.8, 0.8 + 1j],
        "O": [0, 1j, 0.8 + 1j, 0.8, 0],
        "Q": [0, 1j, 0.8 + 1j, 0.8, 0.6 + 0.2j, 0.9 - 0.1j, 0.8, 0],
        "P": [0, 1j, 0.8 + 1j, 0.8 + 0.5j, 0.5j],
        "R": [0, 1j, 0.8 + 1j, 0.8 + 0.6j, 0.5j, 0.8],
        "S": [0.8 + 1j, 0.9j, 0.6j, 0.8 + 0.4j, 0.8 + 0.1j, 0],
        "T": [0.4, 0.4 + 1j, 1j, 0.8 + 1j],
        "U": [1j, 0.1, 0.7, 0.8 + 1j],
        "V": [1j, 0.4, 0.8 + 1j],
        "W": [1j, 0.2, 0.4 + 1j, 0.6, 0.8 + 1j],
        "X": [1j, 0.8, 0.4 + 0.5j, 0.8 + 1j, 0],
        "Y": [1j, 0.4 + 0.5j, 0.8 + 1j, 0.4 + 0.5j, 0.4],
        "Z": [1j, 0.8 + 1j, 0, 0.8],
        " ": [],
    }

    return np.array(__letters[x.upper()])


@app.function
def series(string: str, n: int, fct) -> list[np.ndarray]:
    from itertools import chain
    from typing import Generator

    def __segment(points: np.ndarray, n: int = 100) -> Generator[np.ndarray, None, None]:
        """
        Each letter is represented by a bunch of points a,b,c,d...
        There are straight segments between two adjacent points
        We represent each such segment as a collection of n auxiliary points
        """
        for a, b in zip(points[:-1], points[1:]):
            yield np.linspace(a.real, b.real, n) + 1j * np.linspace(a.imag, b.imag, n)


    segments = []
    for i, _letter in enumerate(string):
        # move pts to the correction position in a word
        pts = letter(_letter) + i

        # move pts to unit square
        pts = 2 * pts / len(string) - 1

        segments.append([fct(z) for z in list(__segment(pts, n=n))])

    # segments is a list of list, flatten it
    return list(chain.from_iterable(segments))


@app.function
def create(name: str, fct: str, event: str, n: int = 100) -> go.Figure:
    from plotly.subplots import make_subplots

    # Create the figure with subplots: 2 rows, 1 column
    def _create_fig() -> go.Figure:
        fig = make_subplots(
            rows=2,
            cols=1,
            row_heights=[0.5, 0.5],  # Top half and bottom half should be equal
            vertical_spacing=0.1,  # Some spacing between the top and bottom sections
            subplot_titles=["", ""],  # No title for the top subplot
        )
        return fig

    def _create_annotation(fig: go.Figure, word: str) -> None:
        # Add the upside-down word as an annotation in the top subplot
        fig.add_annotation(
            x=0.5,  # X position (center)
            y=1,  # Y position at the top of the subplot
            text=word,  # The word to display
            showarrow=False,  # No arrow needed
            font=dict(size=20, color="blue"),  # Text styling: large, blue font
            textangle=180,  # Rotate text by 180 degrees (upside down)
            align="center",  # Center alignment
            valign="middle",  # Vertical alignment (centered)
            row=1,
            col=1,  # Place in the top subplot
        )

    def _remove_axis(fig: go.Figure) -> go.Figure:
        # Update layout settings
        fig.update_layout(
            plot_bgcolor="white",  # White background for clean look
            paper_bgcolor="white",  # White paper background
            showlegend=False,  # No legend needed
            margin=dict(l=30, r=30, t=30, b=30),  # Margins around the plot
        )

        # Update axes settings for the top subplot (hide grid, ticks, and lines)
        fig.update_xaxes(
            row=1,
            col=1,
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            showline=False,
        )
        fig.update_yaxes(
            row=1,
            col=1,
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            showline=False,
        )

        # Update axes settings for the bottom subplot (show gridlines and labels)
        fig.update_xaxes(
            row=2,
            col=1,
            showgrid=True,
            zeroline=False,
            showticklabels=False,
            showline=False,
        )
        fig.update_yaxes(
            row=2,
            col=1,
            showgrid=True,
            zeroline=False,
            showticklabels=False,
            showline=False,
        )
        return fig

    def _plot_letters(fig: go.Figure, d: list[np.ndarray]) -> None:
        # Create traces for each segment
        traces = []

        for segment in d:
            trace = go.Scatter(
                x=segment.real,  # Real part of the complex number
                y=segment.imag,  # Imaginary part of the complex number
                mode="markers+lines",  # Display both markers and lines
                showlegend=False,
                line={"width": 3, "color": "blue"},  # Line style
                marker={"size": 3, "color": "blue"},  # Marker style
            )
            traces.append(trace)

        # Add all traces to the bottom subplot
        for trace in traces:
            fig.add_trace(trace, row=2, col=1)



    # Create the figure with subplots: 2 rows, 1 column
    fig = _create_fig()
    _create_annotation(fig, word=f"{name}<br>{fct}<br>{event}")

    segments = list(series(name, n=n, fct=function_map()[fct]))

    _plot_letters(fig, segments)
    _remove_axis(fig)
    return fig


@app.cell
def __input_name(mo):
    name = mo.ui.text(placeholder="Name...")
    mo.md(
        f"""
        Enter the name of the guest: {name}
        """
    )
    return (name,)


@app.cell
def __input_function(mo):

    # Create dropdown with function names
    options = list(function_map().keys())
    dropdown = mo.ui.dropdown(options=options, value="sinh(3*z)")

    # Display the dropdown
    mo.md(
        f"""
        Enter the complex function: {dropdown}
        """
    )

    # Return both the dropdown and the function map
    return (dropdown,)


@app.cell
def __input_event(mo):
    event = mo.ui.text(placeholder="Event...")
    mo.md(
        f"""
        Enter the name of the event: {event}
        """
    )
    return (event,)


@app.cell
def __output(dropdown, event, mo, name):
    from io import StringIO

    fig = create(name=name.value, fct=dropdown.value, event=event.value, n=100)

    # Export Plotly figure to PNG bytes
    buf = StringIO()
    fig.write_html(buf, include_plotlyjs="cdn")
    buf.seek(0)

    # Display the Plotly chart and provide a download button
    mo.vstack([
        mo.ui.plotly(fig),
        mo.md(create_download_link(
            data=buf.read(),
            filename=f"{name.value}_{event.value}_plot.html"
        ))
    ])
    return


if __name__ == "__main__":
    app.run()
