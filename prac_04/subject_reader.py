FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_data()


def display_data():
    data_file = open(FILENAME)
    for line in data_file:
        line = line.strip().split(',')
        print("{} is taught by {:<12s} and has {:>3d} students".format(line[0], line[1], int(line[2])))
    data_file.close()


def get_data():
    input_file = open(FILENAME)
    list_of_lists = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        list_of_lists.append(parts)
    return list_of_lists
    input_file.close()


main()
