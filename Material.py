from abc import ABC, abstractmethod


class Material(ABC):

    @property
    @abstractmethod
    def stopping_power(self):
        pass

    @property
    def stopping_power_units(self):
        return 'MeV/cm'


class Water(Material):

    @property
    def stopping_power(self):
        return 2
