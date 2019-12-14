from abc import ABC

import numpy as np

from constants import Constants
from triple.Triple import Position, Direction


class Particle(ABC):

    def __init__(self,
                 energy=0,
                 position=Position(),
                 direction=Direction(),
                 generation=0):
        self.energy = energy
        self.position = position
        self.direction = direction
        self.generation = generation

    def advance(self, distance: float):
        self.position += distance

    def rotate(self, theta=None, phi=None):
        self.direction.rotate(theta, phi)

    def increment_generation(self):
        self.generation += 1

    def next_interaction(self, mu: np.array):
        pass

    def compton(self):
        pass

    def pair(self):
        pass


class Photon(Particle):
    mass = 0

    def __init__(self, *args):
        super().__init__(*args)

    def __copy__(self):
        return Photon(self.energy, self.position.__copy__(), self.direction.__copy__(), self.generation)


class Electron(Particle):
    mass = Constants.electron_mass

    def __init__(self, *args):
        super().__init__(*args)

    def __copy__(self):
        return Electron(self.energy, self.position.__copy__(), self.direction.__copy__(), self.generation)


class Positron(Particle):
    mass = Constants.electron_mass

    def __init__(self, *args):
        super().__init__(*args)

    def __copy__(self):
        return Positron(self.energy, self.position.__copy__(), self.direction.__copy__(), self.generation)


if __name__ == '__main__':
    pass
