EMAIL_TO_NAME = {}


def user_name(user_email):
    split_name1 = user_email.split("@")
    full_name = split_name1[0]
    split_name2 = full_name.split(".")
    name = ' '.join(split_name2).title()

    user_reply = input("Is your name {}? (Y/n) ".format(name)).lower()
    if user_reply == "" or user_reply == "y" or user_reply == "yes":
        EMAIL_TO_NAME[user_email] = name
    else:
        name = input("Name: ").title()
        EMAIL_TO_NAME[user_email] = name


user_email = input("Email: ")
while user_email != "":
    if user_email != "":
        user_name(user_email)
    else:
        print("Invalid user email")
    user_email = input("Email: ")

print()
for (email, name) in EMAIL_TO_NAME.items():
    print("{} ({})".format(name, email))

# Email: lindsay.ward@jcu.edu.au
# Is your name Lindsay Ward? (Y/n)
# Email: abe@gmail.com
# Is your name Abe? (Y/n) y
# Email: jimbo546@hotmail.com
# Is your name Jimbo546? (Y/n) no
# Name: Jim Boh
# Email: