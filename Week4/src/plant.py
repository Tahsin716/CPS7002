from week4.src.living_thing import LivingThing


class Plant(LivingThing):

    def __init__(self, name, age, energy):
        super().__init__(name, age, energy)

    def __repr__(self):
        super().__repr__()

    def __str__(self):
        super().__str__()

    def absorb(self, energy):
        self._energy += energy
        residual_energy = self._energy - LivingThing.MAX_ENERGY
        self._energy = LivingThing.MAX_ENERGY if self._energy > LivingThing.MAX_ENERGY else self._energy

        return residual_energy


