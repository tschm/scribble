import marimo

__generated_with = "0.9.29"
app = marimo.App()


@app.cell
def __():
    import marimo as mo

    return (mo,)


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
    dropdown = mo.ui.dropdown(options=options)
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
def __output(mo, name, dropdown, event):
    mo.md(
        f"""
    ### Submitted Strings
    1. First String: **{name.value}**
    2. Second String: **{dropdown.value}**
    3. Third String: **{event.value}**
    """
    )
    print(dropdown.value)
    print(name.value)
    print(event.value)

    empty = False
    for value in [dropdown.value, event.value, name.value]:
        if value == "":
            empty = True

    if not empty:
        print("Try graph")

    return


if __name__ == "__main__":
    app.run()
