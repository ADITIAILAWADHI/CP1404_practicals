def main():
    password_length = int(input("Password length: "))
    password = get_password(password_length)
    display_password(password)


def display_password(password):
    print("Password: ", end="")
    for i in range(len(password)):
        print("*", end="")


def get_password(password_length):
    input_password = input("write a password: ")
    while len(input_password) < password_length:
        input_password = input("write a password: ")
    return input_password


main()
