from prac_06.guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar1.get_age())
    print(guitar1.is_vintage())
    guitar2 = Guitar("Another Guitar", 2013, 16035.40)

    print()
    print("{} get_age() - Expected {}. Got {}".format(guitar1.name, 99, guitar1.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(guitar2.name, 8, guitar2.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar1.name, True, guitar1.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar2.name, False, guitar2.is_vintage()))

    print()
    if guitar1.is_vintage():
        print("{} is_vintage() - Expected {}. Got {}".format(guitar1.name, True, guitar1.is_vintage()))
    else:
        print("50 - year old guitar is_vintage() - Expected {}. Got {}".format(True, guitar1.is_vintage()))


main()
