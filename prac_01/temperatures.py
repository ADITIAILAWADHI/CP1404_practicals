"""
Temperature Conversion program
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)

user_input = input("Choose one option: ").upper()

while user_input != "Q":
    if user_input == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} C = {:.2f} F".format(celsius, fahrenheit))
    elif user_input == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} F = {:.2f} C".format(fahrenheit, celsius))
    else:
        print("Invalid option")
    print(MENU)
    user_input = input("Choose one option: ").upper()
print("Thank You")
