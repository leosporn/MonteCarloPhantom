from abc import ABC
from math import sin, cos, acos, atan2

import numpy as np

from RNG import RNG


class Vector(ABC):
    __slots__ = ['v']

    def __init__(self, v=None):
        if v is None:
            v = [0, 0, 0]
        self.v = np.array(v, dtype=np.float)
        assert len(self) == 3

    def __getitem__(self, idx):
        return self.v[idx]

    def __setitem__(self, idx, value):
        self.v[idx] = value

    def __iter__(self):
        return iter(self.v)

    def __len__(self):
        return self.v.size

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.__class__(self.v + other.v)
        return self.__class__(self.v + other)

    def __neg__(self):
        return self.__class__(-self.v)

    def __sub__(self, other):
        return self.__class__(self.v + -other)

    def __mul__(self, other):
        return self.__class__(self.v * other)

    def __truediv__(self, other):
        return self * (1 / other)

    def __abs__(self):
        return np.linalg.norm(self.v)

    def __repr__(self):
        s = ', '.join(f'{coord:.2f}' for coord in self)
        return f'({s:s})'

    def copy(self):
        return self.__class__(self.v)


class Position(Vector):
    pass


class Direction(Vector):
    rng = RNG()

    @classmethod
    def from_angle(cls, theta=None, phi=None):
        d = cls((0, 0, 1))
        d.rotate(theta, phi)
        return d

    @property
    def theta(self):
        return acos(self[2])

    @property
    def phi(self):
        return atan2(self[1], self[0])

    def rotate(self, theta=None, phi=None, normalize=True):
        if theta is None:
            theta = self.rng.theta
        if phi is None:
            phi = self.rng.phi
        theta0, phi0 = self.theta, self.phi
        st0, ct0, sp0, cp0 = sin(theta0), cos(theta0), sin(phi0), cos(phi0)
        st1, ct1, sp1, cp1 = sin(theta), cos(theta), sin(phi), cos(phi)
        self.v = np.array([
            cp0 * ct1 * st0 - sp0 * sp1 * st1 + cp0 * cp1 * ct0 * st1,
            sp0 * ct1 * st0 + cp0 * sp1 * st1 + sp0 * cp1 * ct0 * st1,
            ct0 * ct1 - cp1 * st0 * st1,
        ])
        if normalize:
            self.normalize()

    def normalize(self):
        self.v /= abs(self)


if __name__ == '__main__':
    P = Position()
    D = Direction.from_angle(0, 0)
