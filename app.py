# content of test_notebook.py

import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def imports():
    import marimo as mo
    import numpy as np
    import plotly.graph_objs as go
    import pytest
    return go, mo, np, pytest

@app.cell(hide_code=True)
def _download(mo):
    import base64

    def create_download_link(data: str, filename: str, mime: str = "text/plain") -> mo.md:
        """
        Create a download link for Marimo notebooks (works in WASM).

        Args:
            data: The string content to download.
            filename: The name of the downloaded file.
            mime: The MIME type of the file (default is "text/plain").

        Returns:
            mo.md object with a download anchor tag.
        """
        b64 = base64.b64encode(data.encode()).decode()
        href = f'data:{mime};base64,{b64}'
        html = f'<a download="{filename}" href="{href}" target="_blank">📥 Download {filename}</a>'
        return mo.md(html)
    return (create_download_link,)


@app.cell(hide_code=True)
def _letter(np):
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

    return (letter,)


@app.cell(hide_code=True)
def _series(letter, np):
    from itertools import chain
    from typing import Generator

    import numexpr as ne

    def series(string: str, n: int, str: str) -> list[np.ndarray]:
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

    return (series,)


@app.cell(hide_code=True)
def _plot(go, np, series):
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

    def create(name: str, fct: str, event: str, n: int = 100) -> go.Figure:
        # Create the figure with subplots: 2 rows, 1 column
        fig = _create_fig()
        _create_annotation(fig, word=f"{name}<br>{fct}<br>{event}")

        segments = list(series(name, n=n, str=fct))

        # d is now a list of list. Flatten it
        # d = list(chain.from_iterable(d))

        _plot_letters(fig, segments)
        _remove_axis(fig)
        return fig

    return (create,)


@app.cell(hide_code=True)
def _test_letter(letter, np):
    def test_letter_returns_array():
        """Test that the letter function returns a numpy array."""
        result = letter("A")
        assert isinstance(result, np.ndarray)

    def test_letter_uppercase():
        """Test that the letter function handles uppercase letters correctly."""
        result = letter("A")
        # A should have 5 points
        assert len(result) == 5
        # First point should be 0
        assert result[0] == 0
        # Second point should be 0.4+1j
        assert result[1] == 0.4 + 1j

    def test_letter_lowercase():
        """Test that the letter function handles lowercase letters correctly."""
        # The function should convert lowercase to uppercase
        upper_result = letter("A")
        lower_result = letter("a")
        np.testing.assert_array_equal(upper_result, lower_result)

    def test_letter_space():
        """Test that the letter function handles spaces correctly."""
        result = letter(" ")
        assert len(result) == 0

    #def test_letter_invalid():
    #    """Test that the letter function raises an error for invalid characters."""
    #    with pytest.raises(KeyError):
    #        letter("1")
    return


@app.cell(hide_code=True)
def _test_series(np, series):
    def test_series_single_letter():
        """Test the series function with a single letter."""
        # Use a simple letter (A) and a simple function (identity)
        result = series("A", n=10, str="z")

        # The result should be a list
        assert isinstance(result, list)

        # The result should not be empty
        assert len(result) > 0

        # Each element in the result should be a numpy array
        for segment in result:
            assert isinstance(segment, np.ndarray)

    def test_series_multiple_letters():
        """Test the series function with multiple letters."""
        # Use two simple letters (AB) and a simple function (identity)
        result = series("AB", n=10, str="z")

        # The result should be a list
        assert isinstance(result, list)

        # The result should not be empty
        assert len(result) > 0

        # Each element in the result should be a numpy array
        for segment in result:
            assert isinstance(segment, np.ndarray)

        # The result for multiple letters should be longer than for a single letter
        single_letter_result = series("A", n=10, str="z")
        assert len(result) > len(single_letter_result)

    def test_series_with_function():
        """Test the series function with a non-trivial function."""
        # Use a simple letter (A) and a non-trivial function (z*z)
        result = series("A", n=10, str="z*z")

        # The result should be a list
        assert isinstance(result, list)

        # The result should not be empty
        assert len(result) > 0

        # Each element in the result should be a numpy array
        for segment in result:
            assert isinstance(segment, np.ndarray)

        # The function z*z should square each point
        # We can't easily test this directly, but we can check that the points are different
        # from the identity function
        identity_result = series("A", n=10, str="z")

        # The results should have the same length
        assert len(result) == len(identity_result)

        # But the points should be different
        # We'll check that at least one segment is different
        # We can't directly compare the segments because they are numpy arrays with complex values
        # So we'll convert them to strings and compare those
        assert any(str(result[i]) != str(identity_result[i]) for i in range(len(result)))
    return


@app.cell(hide_code=True)
def _test_plots(create, go):

    def test_create_returns_figure():
        """Test that the create function returns a plotly Figure."""
        fig = create("Thomas", "sinh(3*z)", "wedding", n=100)
        assert isinstance(fig, go.Figure)

    def test_create_with_different_parameters():
        """Test that the create function works with different parameters."""
        # Test with different name
        fig1 = create("Test", "sinh(3*z)", "wedding", n=100)
        assert isinstance(fig1, go.Figure)

        # Test with different function
        fig2 = create("Thomas", "z*z", "wedding", n=100)
        assert isinstance(fig2, go.Figure)

        # Test with different event
        fig3 = create("Thomas", "sinh(3*z)", "test", n=100)
        assert isinstance(fig3, go.Figure)

        # Test with different n
        fig4 = create("Thomas", "sinh(3*z)", "wedding", n=50)
        assert isinstance(fig4, go.Figure)

    def test_create_with_empty_name():
        """Test that the create function works with an empty name."""
        fig = create("", "sinh(3*z)", "wedding", n=100)
        assert isinstance(fig, go.Figure)

    return


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
    options = ["tanh((-1+2j)*z)", "sinh(3*z)", "exp((-1+2j)*z)"]
    dropdown = mo.ui.dropdown(options=options, value="sinh(3*z)")
    mo.md(
        f"""
        Enter the complex function: {dropdown}
        """
    )
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
def __output(create, create_download_link, dropdown, event, mo, name):
    from io import StringIO

    fig = create(name=name.value, fct=dropdown.value, event=event.value, n=100)

    # Export Plotly figure to PNG bytes
    buf = StringIO()
    fig.write_html(buf, include_plotlyjs="cdn")
    buf.seek(0)

    # Display the Plotly chart and provide a download button
    mo.vstack([
        mo.ui.plotly(fig),
        create_download_link(
            data=buf.read(),
            filename=f"{name.value}_{event.value}_plot.html"
        )
    ])
    return


if __name__ == "__main__":
    app.run()
