import random
quick_picks = int(input("How many quick picks? "))


def quick_pick(a):
    for i in range(0, 6):
        new_item = random.randint(1, 45)
        while new_item in a:
            new_item = random.randint(1, 45)
        a.append(new_item)
    a.sort()
    for k in a:
        print("{:2d}".format(k), end=" ")


for j in range(0, quick_picks):
    quick_pick(a=[])
    print()
