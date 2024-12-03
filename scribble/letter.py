import numpy as np


def letter(x):
    # I have copied this data straight from
    # https://github.com/asgeirbirkis/chebfun/blob/master/scribble.m
    __letters = {
        "A": [0, 0.4 + 1j, 0.8, 0.6 + 0.5j, 0.2 + 0.5j],
        "B": [0, 1j, 0.8 + 0.9j, 0.8 + 0.6j, 0.5j, 0.8 + 0.4j, 0.8 + 0.1j, 0],
        "C": [0.8 + 1j, 0.8j, 0.2j, 0.8],
        "D": [0, 0.8 + 0.1j, 0.8 + 0.9j, 1j, 0],
        "E": [0.8 + 1j, 1j, 0.5j, 0.5j + 0.7, 0.5j, 0, 0.8],
        "F": [0.8 + 1j, 1j, 0.5j, 0.5j + 0.7, 0.5j, 0],
        "G": [0.8 + 1j, 0.8j, 0.2j, 0.6, 0.6 + 0.5j, 0.4 + 0.5j, 0.8 + 0.5j],
        "H": [0, 1j, 0.5j, 0.5j + 0.8, 0.8 + 1j, 0.8],
        "I": [0, 0.8, 0.4, 0.4 + 1j, 1j, 0.8 + 1j],
        "J": [0, 0.4, 0.4 + 1j, 1j, 0.8 + 1j],
        "K": [0, 1j, 0.5j, 0.8 + 1j, 0.5j, 0.8],
        "L": [1j, 0, 0.8],
        "M": [0, 0.1 + 1j, 0.4, 0.7 + 1j, 0.8],
        "N": [0, 1j, 0.8, 0.8 + 1j],
        "O": [0, 1j, 0.8 + 1j, 0.8, 0],
        "Q": [0, 1j, 0.8 + 1j, 0.8, 0.6 + 0.2j, 0.9 - 0.1j, 0.8, 0],
        "P": [0, 1j, 0.8 + 1j, 0.8 + 0.5j, 0.5j],
        "R": [0, 1j, 0.8 + 1j, 0.8 + 0.6j, 0.5j, 0.8],
        "S": [0.8 + 1j, 0.9j, 0.6j, 0.8 + 0.4j, 0.8 + 0.1j, 0],
        "T": [0.4, 0.4 + 1j, 1j, 0.8 + 1j],
        "U": [1j, 0.1, 0.7, 0.8 + 1j],
        "V": [1j, 0.4, 0.8 + 1j],
        "W": [1j, 0.2, 0.4 + 1j, 0.6, 0.8 + 1j],
        "X": [1j, 0.8, 0.4 + 0.5j, 0.8 + 1j, 0],
        "Y": [1j, 0.4 + 0.5j, 0.8 + 1j, 0.4 + 0.5j, 0.4],
        "Z": [1j, 0.8 + 1j, 0, 0.8],
        " ": [],
    }

    return np.array(__letters[x.upper()])
