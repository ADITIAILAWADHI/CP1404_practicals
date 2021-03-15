import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# 10
# What was the smallest number you could have seen, what was the largest?
# Smallest number could be 5 and largest number could be 20.

# What did you see on line 2?
# 5
# What was the smallest number you could have seen, what was the largest?
# Smallest number could be 3 and largest number could be 9.
# Could line 2 have produced a 4?
# No, the only possible outputs could be 3, 5, 7, 9.

# What did you see on line 3?
# 3.3114135131999207
# What was the smallest number you could have seen, what was the largest?
# # Smallest number could be 2.5 and largest number could be 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))  # line 4
