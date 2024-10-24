from week4.src.flying_super_power import FlyingSuperPower
from week4.src.human import Human


class SuperHuman(Human, FlyingSuperPower):

    MINIMUM_ENERGY_REQUIRED_TO_FLY = 5

    def __init__(self, name : str, age : int, energy : int):
        super().__init__(name, age, energy)

    def fly(self, distance: int):
        energy_required = self._energy - distance

        if energy_required < SuperHuman.MINIMUM_ENERGY_REQUIRED_TO_FLY:
            return

        self._energy -= distance

