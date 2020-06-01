from Beam import Beam6MV
from Vector import Position, Direction

if __name__ == '__main__':
    beam = Beam6MV(
        position=Position([0, 0, -100]),
        direction=Direction.from_angle(theta=0, phi=0),
        spread=1e-2,
        n_particles=10
    )
    phantom = None

    for photon in beam:
        photon.propagate(distance=100)
        print(photon)
        print()
