"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
finished = False
result = 0
while not finished:
    try:
        user_marks = int(input("Enter your marks: "))
        finished = True
        result += user_marks
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
