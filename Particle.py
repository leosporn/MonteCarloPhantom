from abc import ABC, abstractmethod

from Vector import Position, Direction


class Particle(ABC):
    __slots__ = ['position', 'direction', 'energy']

    def __init__(self, position=None, direction=None, energy=0):
        if position is None:
            position = Position()
        if direction is None:
            direction = Direction.from_angle()
        self.position = position
        self.direction = direction
        self.energy = energy

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def charge(self):
        pass

    @property
    @abstractmethod
    def mass(self):
        pass

    @property
    def position_units(self):
        return 'cm'

    @property
    def mass_units(self):
        return 'MeV'

    def propagate(self, distance):
        self.position += self.direction * distance

    def deflect(self, theta=None, phi=None):
        self.direction.rotate(theta, phi)

    def __repr__(self):
        return '\n'.join([
            f'{self.name}:',
            f'\t{"Position:":11}{str(self.position)}',
            f'\t{"Direction:":11}{str(self.direction)}',
            f'\t{"Energy:":11}{str(self.energy)}',
        ])


class Photon(Particle):

    @property
    def name(self):
        return 'Photon'

    @property
    def charge(self):
        return 0

    @property
    def mass(self):
        return 0


class ChargedParticle(Particle, ABC):

    @property
    def mass(self):
        return 0.511

    @property
    def alpha(self):
        return self.energy / self.mass


class Electron(ChargedParticle):

    @property
    def name(self):
        return 'Electron'

    @property
    def charge(self):
        return -1


class Positron(ChargedParticle):

    @property
    def name(self):
        return 'Positron'

    @property
    def charge(self):
        return +1


if __name__ == '__main__':
    X = Photon()
    E = Electron()
    P = Positron()
