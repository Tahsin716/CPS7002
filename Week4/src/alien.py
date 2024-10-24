from week4.src.flying_super_power import FlyingSuperPower
from week4.src.force_field_power import ForceFieldPower
from week4.src.invisibility_super_power import InvisibilitySuperPower
from week4.src.living_thing import LivingThing
from week4.src.super_powers import SuperPowers


class Alien(LivingThing, FlyingSuperPower, InvisibilitySuperPower, ForceFieldPower):
    MINIMUM_ENERGY_REQUIRED_TO_FLY = 5
    MINIMUM_ENERGY_REQUIRED_TO_TURN_INVISIBLE = 3

    def __init__(self, name, age, energy, super_powers : list[SuperPowers]):
        super().__init__(name, age, energy)
        self.__super_powers = super_powers
        self.__is_visible = True


    def fly(self, distance: int):
        if not self.__super_powers.__contains__(SuperPowers.FLYING_SUPER_POWER):
            return

        energy_required = self._energy - distance

        if energy_required < Alien.MINIMUM_ENERGY_REQUIRED_TO_FLY:
            return

        self._energy -= distance

    def turn_visible(self):
        if Alien._energy < Alien.MINIMUM_ENERGY_REQUIRED_TO_TURN_INVISIBLE:
            return

        self.__is_visible = False

    def turn_invisible(self):
        self.__is_visible = True

    def generate_force_field(self):
        if not self.__super_powers.__contains__(SuperPowers.GENERATE_FORCE_FIELD):
            return

        print("Generate Force Field!")



