"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    rules = """\t1 or more uppercase characters
    \t1 or more lowercase characters
    \t1 or more numbers"""
    print(rules)
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: {}".format(SPECIAL_CHARACTERS))
    password = input("Password: ")
    while not is_valid_password(password):
        print("Invalid password! Try again")
        password = input("Password: ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1

        if char.isupper():
            count_upper += 1

        if char.isdigit():
            count_digit += 1

        if SPECIAL_CHARS_REQUIRED:
            if char in SPECIAL_CHARACTERS:
                count_special += 1

    if SPECIAL_CHARS_REQUIRED:
        if count_lower == 0 or count_upper == 0 or count_digit == 0 or count_special == 0:
            return False
    else:
        if count_lower == 0 or count_upper == 0 or count_digit == 0:
            return False

    return True


main()
