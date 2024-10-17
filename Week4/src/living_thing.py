class LivingThing:
    MAX_ENERGY = 100
    MIN_ENERGY = 20
    REPRODUCE_ENERGY = 10

    _age = 0
    _energy = 100
    _name = "Default Name"

    def __init__(self, name, age, energy):
        self._name = name
        self._age = age
        self._energy = energy

    def __repr__(self):
        return f'living thing (name={self._name}, age={self._age}), energy={self._energy}'

    def __str__(self):
        return f'{self._name} is {self._age} years old with {self._energy} energy'

    def grow(self):
        self._age += 1

    def reproduce(self):
        if self._energy - LivingThing.REPRODUCE_ENERGY < LivingThing.MIN_ENERGY:
            return False

        self._energy -= LivingThing.REPRODUCE_ENERGY

        return True
