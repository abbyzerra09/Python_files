class Car:
    def __init__(self, colour, model, year):
        self.colour = colour
        self.model = model
        self.year = year
        self.fuel_level = 100
        self.engine_on = False

    def start_engine(self):
        if self.engine_on:
            print("Engine is already on.")
        elif self.fuel_level > 0:
            self.engine_on = True
            print("Engine started")
        else:
            print("No fuel. Cannot start engine.")

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            print("Engine stopped")
        else:
            print("Engine is already off.")

    def refuel(self, amount):
        self.fuel_level += amount
        print(f"Refuelling with {amount} litres of fuel.")

    def drive(self, distance):
        fuel_used = distance / 10
        if self.engine_on == False:
            print("Engine is off. Cannot drive.")
        elif fuel_used > self.fuel_level:
            print("Not enough fuel to cover the distance.")
        else:
            self.fuel_level -= fuel_used
            print(f"Drove {distance} km.")

    def display_info(self):
        if self.engine_on:
            engine_status = "on"
        else:
            engine_status = "off"
        print(f"{self.year} {self.colour} {self.model} | Fuel Level: {self.fuel_level} | Engine: {engine_status}")


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

    # Displaying updated information. added rohit thapa as a test signal
    my_car.display_info()