"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MIN_SCORE = 0
MAX_SCORE = 100

score = float(input("Enter score: "))
while score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score \nPlease enter score between {} and {}".format(MIN_SCORE, MAX_SCORE))
    score = float(input("Enter score: "))

if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Bad")

print("Thank You")
