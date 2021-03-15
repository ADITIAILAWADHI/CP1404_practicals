import random
text_file = open("results.txt", "w")


def main():
    user_input = int(input("number of scores: "))
    for i in range(user_input):
        score = random.randint(0, 100)
        result = score_calculator(score)
        print("{} is {}".format(score, result), file=text_file)


def score_calculator(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
