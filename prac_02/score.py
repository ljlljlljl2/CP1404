"""Program to determine score results for user and random scores."""

import random


def main():
    """Get a user score and random score, then display their results."""
    user_score = float(input("Enter score: "))
    user_result = determine_score_status(user_score)
    print(f"User score {user_score} is {user_result}")

    if user_result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(0, 100)
    random_result = determine_score_status(random_score)
    print(f"Random: {random_score} = {random_result}")


def determine_score_status(score):
    """Determine the result for a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


main()