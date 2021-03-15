import random
text_file = open("temps_input.txt", "w")
text_file2 = open("temps_output.txt", "w")


def main():
    for i in range(15):
        print(random.uniform(-200, 200), file=text_file)

    text_file.close()
    text_file3 = open("temps_input.txt", "r")

    for i in text_file3:
        degrees_celsius = fahrenheit_to_celsius(float(i))
        print(degrees_celsius, file=text_file2)

    text_file2.close()
    text_file3.close()


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()
