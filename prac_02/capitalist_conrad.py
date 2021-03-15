"""
CP1404/CP5632 - Practical
"""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0

OUTPUT_FILE = "stock_price.txt"
out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price), file=out_file)
day = 1

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day", str(day), "price is: ${:,.2f}".format(price), file=out_file)
    day += 1

out_file.close()
print("Code executed")
