import unittest

from week4.src.living_thing import LivingThing


class TestLivingThing(unittest.TestCase):
    def test_grow(self):
        living_thing = LivingThing("Human", 20, 80)
        living_thing.grow()

        self.assertEqual(living_thing._age, 21, "Age should be 21")
        self.assertEqual(living_thing.reproduce(), True, "Enough energy to reproduce")

        living_thing = LivingThing("Human", 20, 10)
        self.assertEqual(living_thing.reproduce(), False, "Not enough energy to reproduce")


if __name__ == "__main__":
    unittest.main()