import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def smallangle():
    pass

@smallangle.command()
@click.option(
    "-n",
    "--number",
    type=int,
    default=5,
)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@smallangle.command()
@click.option(
    "-n",
    "--number",
    type=int,
    default=5,)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    smallangle()