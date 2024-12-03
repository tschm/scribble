import marimo as mo

__generated_with = "0.9.29"
app = mo.App()


@app.cell
def inputs():
    string1 = mo.ui.text(label="First String")
    string2 = mo.ui.text(label="Second String")
    string3 = mo.ui.text(label="Third String")
    submit_button = mo.ui.button(label="Submit")

    return string1, string2, string3, submit_button


@app.cell
def output(string1, string2, string3, submit_button):
    result = mo.md(
        f"""
    ### Submitted Strings

    {submit_button()}

    1. First String: **{string1.value}**
    2. Second String: **{string2.value}**
    3. Third String: **{string3.value}**
    """
    )

    return result


if __name__ == "__main__":
    app.run()
