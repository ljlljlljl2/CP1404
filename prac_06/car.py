"""CP1404 Practical 06 - Car class."""


class Car:
    """Represent a Car object."""

    def __init__(self, name, fuel=0):
        """Initialise a Car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """Add the given amount of fuel to the car."""
        self.fuel += amount

    def drive(self, distance):
        """
        Drive the car a given distance.

        Return the actual distance driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance

        self.odometer += distance
        return distance

    def __str__(self):
        """Return string representation of car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"