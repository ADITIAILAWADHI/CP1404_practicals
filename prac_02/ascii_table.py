LOWER = 33
UPPER = 127

user_input = input("Enter a character: ")
a = ord(user_input)
print("The ASCII code for g is {}".format(a))

user_input = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while user_input < LOWER or user_input > UPPER:
    user_input = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
a = chr(user_input)
print("The character for {} is {}".format(user_input, a))

for i in range(LOWER, UPPER):
    print("{} {}".format(i, chr(i)))
