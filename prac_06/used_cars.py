from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "my_car")
    my_car.drive(30)
    print("my_car:")
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    print("\nlimo:")
    limo = Car(100, "limo")
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)

    print("\nDisplay:")
    print(my_car)
    print(limo)


main()
