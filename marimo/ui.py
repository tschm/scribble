import marimo

__generated_with = "0.9.30"
app = marimo.App()


@app.cell
def __():
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
    fig = create(name=name.value, fct=dropdown.value, event=event.value, n=100)
    mo.vstack(
        [
            mo.ui.plotly(fig),
        ]
    )
    return (fig,)


if __name__ == "__main__":
    app.run()
