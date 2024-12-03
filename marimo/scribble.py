import marimo

__generated_with = "0.9.28"
app = marimo.App()


@app.cell
def __():
    import matplotlib.pyplot as plt
    import numpy as np

    from pyscribble.scribble import scribble

    return np, plt, scribble


@app.cell
def __(plt, scribble):
    def wedding(word, f, title):
        fig, axes = plt.subplots(
            nrows=2, ncols=1, figsize=(8.27, 11.69), subplot_kw={"aspect": "equal"}
        )

        scribble(axes[1], text=word, f=f, title=title, linewidth=2, color="blue")

        axes[0].set_axis_off()
        axes[0].text(
            0.5,
            0.5,
            "{name}\n{function}".format(name=word, function=f),
            horizontalalignment="right",
            rotation=180,
        )

        fig.savefig("data/{name}.pdf".format(name=word))
        fig.savefig("data/{name}.png".format(name=word))

    return (wedding,)


@app.cell
def __(EasyForm):
    form = EasyForm("Create a name tag")
    form.addTextField("Text")
    form["Text"] = "Hans Dampf"
    form.addTextField("Title")
    form["Title"] = "I am the title"
    form.addTextField("Function")
    form["Function"] = "tanh((-1+2j)*z)"
    form.addButton("Go!", tag="run")
    form
    return (form,)


@app.cell
def __(form, wedding):
    # Cell tags: run
    wedding(form["Text"], f=form["Function"], title=form["Title"])
    return


@app.cell
def __():
    import pandas as pd

    return (pd,)


@app.cell
def __(pd, wedding):
    frame = pd.read_csv("names.csv", header=0)
    for index, row in frame.iterrows():
        wedding(word=row["Name"], f=row["Function"], title="Lydia & Thomas")
    return frame, index, row


if __name__ == "__main__":
    app.run()
