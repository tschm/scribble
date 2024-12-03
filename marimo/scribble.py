import marimo

__generated_with = "0.9.29"
app = marimo.App()


@app.cell
def __(__file__):
    from pathlib import Path

    import matplotlib.pyplot as plt

    from pyscribble.scribble import wedding

    path = Path(__file__).parent
    return Path, path, plt, wedding


@app.cell
def __(path, plt, wedding):
    with open(path / "input" / "names.csv") as f:
        for line in f:
            name, func = line.split(",")
            wedding(word=name, f=func, title="Wedding Lydia & Thomas")
            # plt.savefig(f"{name}.png")
            plt.show()
    return f, func, line, name


if __name__ == "__main__":
    app.run()
