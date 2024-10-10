class Human:
    MAX_ENERGY = 100
    ENERGY_REQUIRED_FOR_REPRODUCTION = 20
    MINIMUM_ENERGY_REQUIRED_TO_MOVE = 10

    def __init__(self, name, age=0, energy=100):
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self):
        return f'human(name={self.name}, age={self.age}), energy={self.energy}'

    def __str__(self):
        return f'{self.name} is {self.age} years old with {self.energy} energy'

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount
        residual_energy = self.energy - Human.MAX_ENERGY
        self.energy = Human.MAX_ENERGY if self.energy > Human.MAX_ENERGY else self.energy

        return residual_energy

    def reproduce(self):
        return self.energy >= Human.ENERGY_REQUIRED_FOR_REPRODUCTION

    def move(self, distance):
        energy_required = self.energy - distance

        if energy_required < Human.MINIMUM_ENERGY_REQUIRED_TO_MOVE:
            return False

        self.energy -= distance

        return True



