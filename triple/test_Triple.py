from unittest import TestCase

import numpy as np

from triple.Triple import Triple, Position, Direction


class TestTriple(TestCase):

    def setUp(self) -> None:
        self.T = Triple

    def test_iterate(self):
        counter = 0
        for _ in self.T():
            counter += 1
        self.assertEqual(3, counter)

    def test_init_0_value(self):
        self.assertTripleEqual([0, 0, 0], self.T())

    def test_init_1_value(self):
        for value in np.random.randn(10):
            self.assertTripleEqual([value, value, value], self.T(value))

    def test_init_2_value(self):
        pass

    def test_init_3_value(self):
        for values in np.random.randn(10, 3):
            value1, value2, value3 = values
            self.assertTripleEqual(values, self.T(value1, value2, value3))

    def test_init_object(self):
        for values in np.random.randn(10, 3):
            for fun in list, tuple, np.array:
                self.assertTripleEqual(values, self.T(fun(values)))

    def test_init_triple(self):
        for values in np.random.randn(10, 3):
            orig = values
            for i in range(10):
                copy = self.T(orig)
                self.assertTripleEqual(orig, copy)
                orig = copy

    def test_xyz(self):
        t = self.T()
        for values in np.random.randn(10, 3):
            t.x, t.y, t.z = values
            self.assertEqual(values[0], t.x)
            self.assertEqual(values[1], t.y)
            self.assertEqual(values[2], t.z)

    def test_combine(self):
        for v1, v2 in np.random.randn(10, 2, 3):
            t1, t2 = self.T(v1), self.T(v2)
            self.assertTripleEqual(v1 + v2, t1 + t2)
            self.assertTripleEqual(v1 - v2, t1 - t2)
            self.assertTripleEqual(v1 * v2, t1 * t2)

    def test_i_combine(self):
        for values in np.random.randn(10, 3):
            t = self.T(values)
            self.assertTripleEqual(values, t)
            t *= t
            self.assertTripleEqual(pow(values, 2), t)
            t -= t
            self.assertTripleEqual(Triple(), t)
            t += values
            self.assertTripleEqual(values, t)
            t *= 1
            self.assertTripleEqual(values, t)

    def assertTripleEqual(self, values, triple):
        for value, item in zip(values, triple):
            self.assertEqual(value, item)

    def assertTripleAlmostEqual(self, values, triple):
        for value, item in zip(values, triple):
            self.assertAlmostEqual(value, item)


class TestPosition(TestTriple):

    def setUp(self) -> None:
        self.T = Position


class TestDirection(TestTriple):

    def setUp(self) -> None:
        self.T = Direction

    def test_init_0_value(self):
        for _ in range(10):
            self.assertIsDirection(Direction())

    def test_init_1_value(self):
        pass

    def test_init_2_value(self):
        for values in np.random.randn(10, 2):
            theta, phi = values
            d = Direction(theta, phi)
            self.assertIsDirection(d)

    def test_init_3_value(self):
        pass

    def test_init_object(self):
        pass

    def test_init_triple(self):
        pass

    def test_random_sample(self):
        total, n_test = np.zeros(3), 10000
        for _ in range(n_test):
            d = Direction()
            total += np.array(d.v)
        self.assertGreater(3 * np.sqrt(n_test), self.norm(Triple(total)))

    def test_rotate_random(self):
        total, n_test, d = np.zeros(3), 10000, Direction()
        for i in range(10):
            d.rotate()
            total += np.array(d.v)
            self.assertIsDirection(d)
        self.assertGreater(3 * np.sqrt(n_test), self.norm(Triple(total)))

    def test_rotate_zero(self):
        for phi in np.random.randn(10):
            d1 = Direction()
            d2 = d1.__copy__()
            d2.rotate(0, phi)
            self.assertGreater(1e-7, self.norm(d1 - d2))

    def test_rotate_pi(self):
        for phi in np.random.randn(10):
            d1 = Direction()
            d2 = d1.__copy__()
            d2.rotate(np.pi, phi)
            self.assertGreater(1e-7, self.norm(d1 + d2))

    def test_rotate_general(self):
        for values in np.random.randn(100, 2):
            theta, phi = values
            d1 = Direction()
            d2 = d1.__copy__()
            d2.rotate(theta, phi)
            self.assertAlmostEqual(np.cos(theta), sum(d1 * d2))

    def test_combine(self):
        pass

    def test_i_combine(self):
        pass

    def assertIsDirection(self, direction):
        self.assertAlmostEqual(1, self.norm(direction))

    def norm(self, triple):
        return pow(sum(triple * triple), 1 / 2)
