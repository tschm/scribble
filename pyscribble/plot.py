import plotly.graph_objs as go
from plotly.subplots import make_subplots

from .scribble import series


# Create the figure with subplots: 2 rows, 1 column
def __create_fig():
    fig = make_subplots(
        rows=2,
        cols=1,
        row_heights=[0.5, 0.5],  # Top half and bottom half should be equal
        vertical_spacing=0.1,  # Some spacing between the top and bottom sections
        subplot_titles=["", ""],  # No title for the top subplot
    )
    return fig


def __create_annotation(fig, word):
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


def __remove_axis(fig):
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


def __plot_letters(fig, d):
    # Create traces for each segment
    traces = []

    for _, segments in d.items():
        for segment in segments:
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


def create(name, fct, n=100):
    # Create the figure with subplots: 2 rows, 1 column
    fig = __create_fig()
    __create_annotation(fig, word=f"{name}<br>{fct}")

    d = dict(series(name, n=n, str=fct))

    __plot_letters(fig, d)
    __remove_axis(fig)
    return fig
