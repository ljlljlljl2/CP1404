"""CP1404 Practical 03 - Capitalist Conrad."""

import random

INITIAL_PRICE = 10.0
MIN_PRICE = 1.0
MAX_PRICE = 100.0
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
FILENAME = "capitalist_conrad_output.txt"

price = INITIAL_PRICE
number_of_days = 0

out_file = open(FILENAME, "w")

print(f"Starting price: ${price:,.2f}")
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    change_type = random.randint(1, 2)

    if change_type == 1:
        change_percent = random.uniform(0, MAX_INCREASE)
        price *= (1 + change_percent)
    else:
        change_percent = random.uniform(0, MAX_DECREASE)
        price *= (1 - change_percent)

    print(f"On day {number_of_days} price is: ${price:,.2f}")
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()