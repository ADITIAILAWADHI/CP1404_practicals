print("odd numbers between 1 and 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")

# a. count in 10s from 0 to 100
print("count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

# b. count down from 20 to 1
print("count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n")

# c. print n stars, all on one line
n = int(input("Number of stars: "))
print("{} stars, all on one line:".format(n))
for i in range(1, n+1):
    print("*", end='')

print("\n")

# d. print n lines of increasing stars
print("{} lines of increasing stars:".format(n))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end='')
    print()
