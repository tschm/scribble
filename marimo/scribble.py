import marimo

__generated_with = "0.9.28"
app = marimo.App()


@app.cell
def __(__file__):
    from pathlib import Path

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    from pyscribble.scribble import scribble

    path = Path(__file__).parent
    return Path, np, path, pd, plt, scribble


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

        plt.show()

    return (wedding,)


@app.cell
def __(wedding):
    text = "Hans Dampf"
    title = "My wedding"
    function = "tanh((-1+2j)*z)"
    wedding(word=text, title=title, f=function)
    return function, text, title


@app.cell
def __(path, pd, wedding):
    frame = pd.read_csv(path / "input" / "names.csv", header=0)
    for index, row in frame.iterrows():
        wedding(word=row["Name"], f=row["Function"], title="Lydia & Thomas")
    return frame, index, row


if __name__ == "__main__":
    app.run()
