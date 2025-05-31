import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def __init():
    import marimo as mo

    from pyscribble import create

    return create, mo


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
def __output(create, dropdown, event, mo, name):
    import base64
    from io import StringIO


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
