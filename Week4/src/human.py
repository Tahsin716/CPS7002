from week4.src.animal import Animal


class Human(Animal):

    def __init__(self, name, age, energy):
        super().__init__(name, age, energy)
        self.__clothing = []

    def __repr__(self):
        super().__repr__()

    def __str__(self):
        super().__str__()

    def dress(self, clothes):
        self.__clothing.append(clothes)

    def undress(self, clothes):
        self.__clothing.remove(clothes)

