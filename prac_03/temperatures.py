def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    user_input = input("Choose one option: ").upper()
    while user_input != "Q":
        if user_input == "C":
            degree_celsius = float(input("Celsius: "))
            degrees_fahrenheit = celsius_to_fahrenheit(degree_celsius)
            print("Result: {:.2f} C = {:.2f} F".format(degree_celsius, degrees_fahrenheit))
        elif user_input == "F":
            degree_fahrenheit = float(input("Fahrenheit: "))
            degrees_celsius = fahrenheit_to_celsius(degree_fahrenheit)
            print("Result: {:.2f} F = {:.2f} C".format(degree_fahrenheit, degrees_celsius))
        else:
            print("Invalid option")
        print(MENU)
        user_input = input("Choose one option: ").upper()
    print("Thank You")


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()
