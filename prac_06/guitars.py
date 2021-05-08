from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print("{} ({}) : ${} added.".format(name, year, cost))
        print()
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    print("\n... snip ...\n")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print("Guitar", str(i), guitar)


main()
