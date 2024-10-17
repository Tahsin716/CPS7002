import unittest

from week4.src.human import Human


class TestHuman(unittest.TestCase):

    def test_eat(self):
        # energy is full and try to eat
        human_prins = Human("Prins", 20, 80)
        self.assertEqual(human_prins.eat(40), 20, "Excess should be 20.")

        # energy is below 100 and eat more than required
        human_prins = Human("Prins", 20, energy=90)
        self.assertEqual(human_prins.eat(20), 10, "Excess should 10.")

        # energy is below 100 and eat exactly what is required
        human_prins = Human("Prins", 20, energy=80)
        self.assertEqual(human_prins.eat(20), 0, "Excess should be 0.")

        # energy is below 100 and eat less than required
        human_prins = Human("Prins", 20, energy=70)
        self.assertEqual(human_prins.eat(20), -10, "Excess should be -10.")

    def test_move(self):
        human_prins = Human("Prins", 20, 80)
        self.assertEqual(human_prins.move(90), False, "Not enough energy to move.")

        human_prins = Human("Prins", 20, 80)
        self.assertEqual(human_prins.move(40), True, "Enough energy to move.")



if __name__ == '__main__':
    unittest.main()
