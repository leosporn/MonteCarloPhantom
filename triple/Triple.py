from rng import RNG


class Triple:

    def __init__(self, *args):
        if len(args) == 1:
            obj = args[0]
            try:
                self.v = [item for item in obj]
            except TypeError:
                self.v = [obj, obj, obj]
        elif len(args) == 3:
            self.v = [arg for arg in args]
        else:
            self.v = [0, 0, 0]

    def __copy__(self):
        return Triple(self)

    def __iter__(self):
        return iter(self.v)

    @property
    def x(self):
        return self.v[0]

    @x.setter
    def x(self, value):
        self.v[0] = value

    @property
    def y(self):
        return self.v[1]

    @y.setter
    def y(self, value):
        self.v[1] = value

    @property
    def z(self):
        return self.v[2]

    @z.setter
    def z(self, value):
        self.v[2] = value

    def __combine(self, other, fun):
        return Triple(fun(x, y) for x, y in zip(self, Triple(other)))

    def __add__(self, other):
        return self.__combine(other, lambda i, j: i + j)

    def __sub__(self, other):
        return self.__combine(other, lambda i, j: i - j)

    def __mul__(self, other):
        return self.__combine(other, lambda i, j: i * j)


class Position(Triple):

    def __init__(self, *args):
        super().__init__(*args)

    def __copy__(self):
        return Position(self)


class Direction(Triple):

    def __init__(self, theta=None, phi=None):
        theta, phi = self.__generate_angles(theta, phi)
        st, ct, sp, cp = self.__get_sin_cos(theta, phi)
        super().__init__(st * cp, st * sp, ct)

    def __copy__(self):
        copy = Direction()
        copy.v = list(item for item in self)
        return copy

    def __generate_angles(self, theta, phi):
        if theta == None:
            theta = RNG.theta()
        if phi == None:
            phi = RNG.phi()
        return theta, phi

    def __get_sin_cos(self, theta, phi):
        return RNG.np.sin(theta), RNG.np.cos(theta), RNG.np.sin(phi), RNG.np.cos(phi)

    def rotate(self, theta=None, phi=None):
        theta, phi = self.__generate_angles(theta, phi)
        st, ct, sp, cp = self.__get_sin_cos(theta, phi)
        stcp, stsp = st * cp, st * sp
        N = pow(1 - pow(self.z, 2), 1 / 2)
        x = ct * self.x + (stsp * self.y - stcp * self.x * self.z) / N
        y = ct * self.y - (stsp * self.x + stcp * self.y * self.z) / N
        z = ct * self.z + stcp * N
        self.x, self.y, self.z = x, y, z


if __name__ == '__main__':
    pass
