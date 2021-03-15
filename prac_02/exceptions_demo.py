"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
It will occur when an invalid value or type is assigned to an object or a built-in function.

2. When will a ZeroDivisionError occur?
It will occur when a number is divided by a value zero which if calculated would give result as an infinite number.
But instead, a ZeroDivisionError occurs.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, scroll down for the solution.
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Solution for 3:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
