from bisect import bisect
from math import acos

import numpy as np


class RNG:
    uniform = np.random.uniform

    @property
    def phi(self):
        return self.uniform(0, 2 * np.pi)

    @property
    def theta(self):
        return acos(self.uniform(-1, +1))

    def phi_pair(self):
        p = self.phi
        return p, p + np.pi

    def sample(self, cdf, items=None):
        if items is None:
            items = range(len(cdf))
        return items[bisect(cdf, self.uniform(cdf[-1]))]


if __name__ == '__main__':
    r = RNG()
