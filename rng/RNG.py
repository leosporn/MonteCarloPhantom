import numpy as np


def phi(n=1):
    phi = np.random.uniform(0, 2 * np.pi)
    if n == 1:
        return phi
    elif n == 2:
        return phi, phi + np.pi


def theta(interaction=None):
    if interaction == None:
        return np.arccos(np.random.uniform(-1, +1))
