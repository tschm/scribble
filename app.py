import marimo

__generated_with = "0.9.30"
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
    return dropdown, options


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
    from io import BytesIO

    fig = create(name=name.value, fct=dropdown.value, event=event.value, n=100)

    img = fig.to_image(format="png")
    # print(img)
    data = BytesIO(img)

    disabled = True
    if dropdown.value and event.value and name.value:
        disabled = False

    # Create a download button for the Plotly graph
    download_btn = mo.download(
        data=data,
        filename=f"{name.value}_{event.value}_plot.png",
        label="Download",
        mimetype="image/png",
        disabled=disabled,
    )

    # Display the plot and download button
    mo.md(
        f"""
    {download_btn}

    {mo.ui.plotly(fig)}
    """
    )

    # return fig, download_btn


if __name__ == "__main__":
    app.run()
