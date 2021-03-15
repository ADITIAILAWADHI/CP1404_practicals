import random
MIN_SCORE = 0
MAX_SCORE = 100


def score_calculator(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def main():
    score = int(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score \nPlease enter score between {} and {}".format(MIN_SCORE, MAX_SCORE))
        score = float(input("Enter score: "))
    result = score_calculator(score)
    print("{} is {}".format(score, result))

    score = random.randint(0, 100)
    result = score_calculator(score)
    print("{} is {}".format(score, result))


main()
