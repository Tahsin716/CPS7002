from week4.src.invisibility_super_power import InvisibilitySuperPower
from week4.src.plant import Plant


class SuperPlant(Plant, InvisibilitySuperPower):
    MINIMUM_ENERGY_REQUIRED_TO_TURN_INVISIBLE = 3

    def __init__(self, name, age, energy):
        super().__init__(name, age, energy)
        self.__is_visible = True

    def turn_invisible(self):
        if Plant._energy < SuperPlant.MINIMUM_ENERGY_REQUIRED_TO_TURN_INVISIBLE:
            return

        self.__is_visible = False

    def turn_visible(self):
        self.__is_visible = True

