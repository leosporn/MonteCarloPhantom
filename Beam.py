from abc import ABC, abstractmethod

import numpy as np

from Particle import Photon
from RNG import RNG

with open('data/6MV_spectrum.txt') as file:
    data = (float(s.replace('\n', '')) for s in file.readlines())
energy_6MV, spectrum_6MV = [], []
for i, x in enumerate(data):
    energy_6MV.append(0.25 * (i + 1))
    spectrum_6MV.append(x)


class Beam(ABC):
    __slots__ = ['particle', 'position', 'direction', 'spread', 'n_particles']
    rng = RNG()

    def __init__(self, particle, position, direction, spread, n_particles):
        self.particle = particle
        self.position = position
        self.direction = direction
        self.spread = spread
        self.n_particles = n_particles

    def __iter__(self):
        return iter(self.new_particle for _ in range(self.n_particles))

    @property
    def new_particle(self):
        particle = self.particle(
            position=self.position.copy(),
            direction=self.direction.copy(),
            energy=self.new_energy
        )
        u = self.rng.uniform(0, self.spread)
        particle.deflect(theta=u)  # TODO
        return particle

    @property
    @abstractmethod
    def new_energy(self):
        pass


class Beam6MV(Beam):
    energy = np.array(energy_6MV)
    spectrum = np.cumsum(spectrum_6MV)

    def __init__(self, position, direction, spread, n_particles):
        super().__init__(Photon, position, direction, spread, n_particles)

    @property
    def new_energy(self):
        return self.rng.sample(self.spectrum, self.energy)
