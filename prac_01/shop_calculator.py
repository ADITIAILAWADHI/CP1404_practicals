"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on screen.
"""

total_items = int(input("Enter total number of items: "))
while total_items < 0:
    print("Invalid number of items!")
    total_items = int(input("Enter total number of items: "))

total_price = 0
for i in range(0, total_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print('Total price for %d items is $%.2f' % (total_items, total_price))
