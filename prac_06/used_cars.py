"""CP1404 Practical 06 - Used cars program."""

from prac_06.car import Car


def main():
    """Demo program for Car class."""
    my_car = Car("My Car", 180)
    limo = Car("Limo", 100)

    limo.add_fuel(20)
    print(f"{limo.fuel} units of fuel")
    print(f"The limo drove {limo.drive(115)}km")
    print(limo)
    print(my_car)


main()