import numpy as np

def letter(x):
    # I have copied this data straight from
    # https://github.com/asgeirbirkis/chebfun/blob/master/scribble.m
    __letters = {
        "A": [0, .4 + 1j, .8, .6 + .5j, .2 + .5j],
        "B": [0, 1j, .8 + .9j, .8 + .6j, .5j, .8 + .4j, .8 + .1j, 0],
        "C": [.8 + 1j, .8j, .2j, .8],
        "D": [0, .8 + .1j, .8 + .9j, 1j, 0],
        "E": [.8 + 1j, 1j, .5j, .5j + .7, .5j, 0, .8],
        "F": [.8 + 1j, 1j, .5j, .5j + .7, .5j, 0],
        "G": [.8 + 1j, .8j, .2j, .6, .6 + .5j, .4 + .5j, .8 + .5j],
        "H": [0, 1j, .5j, .5j + .8, .8 + 1j, .8],
        "I": [0, .8, .4, .4 + 1j, 1j, .8 + 1j],
        "J": [0, .4, .4 + 1j, 1j, .8 + 1j],
        "K": [0, 1j, .5j, .8 + 1j, .5j, .8],
        "L": [1j, 0, .8],
        "M": [0, .1 + 1j, .4, .7 + 1j, .8],
        "N": [0, 1j, .8, .8 + 1j],
        "O": [0, 1j, .8 + 1j, .8, 0],
        "Q": [0, 1j, .8 + 1j, .8, .6 + .2j, .9 - .1j, .8, 0],
        "P": [0, 1j, .8 + 1j, .8 + .5j, .5j],
        "R": [0, 1j, .8 + 1j, .8 + .6j, .5j, .8],
        "S": [.8 + 1j, .9j, .6j, .8 + .4j, .8 + .1j, 0],
        "T": [.4, .4 + 1j, 1j, .8 + 1j],
        "U": [1j, .1, .7, .8 + 1j],
        "V": [1j, .4, .8 + 1j],
        "W": [1j, .2, .4 + 1j, .6, .8 + 1j],
        "X": [1j, .8, .4 + .5j, .8 + 1j, 0],
        "Y": [1j, .4 + .5j, .8 + 1j, .4 + .5j, .4],
        "Z": [1j, .8 + 1j, 0, .8],
        " ": []
    }

    return np.array(__letters[x.upper()])