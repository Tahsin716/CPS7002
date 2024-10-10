class Car:

    def __init__(self, colour, model, year, fuel_level=100, engine_on=False):
        self.__colour = colour
        self.__model = model
        self.__year = year
        self.__fuel_level = fuel_level
        self.__engine_on = engine_on

    def start_engine(self):
        if self.__engine_on:
            print("The engine has already been started")
            return

        if self.__fuel_level > 0:
            self.__engine_on = True
            print("The car engine has started.")
        else:
            self.__engine_on = False
            print("No fuel. Cannot start engine.")

    def stop_engine(self):
        if self.__engine_on:
            self.__engine_on = False
            print("The car engine has stopped.")
        else:
            print("The car engine is already off.")

    def refuel(self, amount):
        self.__fuel_level += amount
        print(f"Refuelling with {amount} litres of fuel.")

    def drive(self, distance):
        if not self.__engine_on:
            print("The car engine is off.")
            return

        fuel_required = distance / 10

        if self.__fuel_level < fuel_required:
            print("Insufficient fuel for the journey.")
            return

        self.__fuel_level -= fuel_required
        print(f"Driving {distance} km.")

    def display_info(self):
        print(
            f"{self.__year} {self.__colour} {self.__model} | Fuel Level: {self.__fuel_level} | Engine: {"On" if self.__engine_on else "Off"}")


if __name__ == "__main__":
    # Creating an instance of car.
    my_car = Car("Silver", "BMW", 2023)

    # Invoking instance methods.
    my_car.start_engine()
    my_car.drive(800)
    my_car.drive(300)
    my_car.refuel(10)
    my_car.drive(300)
    my_car.stop_engine()

    # Displaying updated information.
    my_car.display_info()
