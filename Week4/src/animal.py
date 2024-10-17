from week4.src.living_thing import LivingThing


class Animal(LivingThing):
    MINIMUM_ENERGY_REQUIRED_TO_MOVE = 10

    def __init__(self, name, age, energy):
        super().__init__(name, age, energy)

    def __repr__(self):
        super().__repr__()

    def __str__(self):
        super().__str__()

    def move(self, distance):
        energy_required = self._energy - distance

        if energy_required < Animal.MINIMUM_ENERGY_REQUIRED_TO_MOVE:
            return False

        self._energy -= distance

        return True

    def eat(self, amount):
        self._energy += amount
        residual_energy = self._energy - LivingThing.MAX_ENERGY
        self._energy = LivingThing.MAX_ENERGY if self._energy > LivingThing.MAX_ENERGY else self._energy

        return residual_energy
