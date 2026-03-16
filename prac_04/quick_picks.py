"""CP1404 Practical 04 - Quick Picks."""

import random

NUMBERS_PER_PICK = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    """Generate quick picks."""
    number_of_picks = int(input("How many quick picks? "))

    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate one quick pick with unique random numbers."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    return quick_pick


main()