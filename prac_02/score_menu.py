"""Menu-driven program for working with scores."""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the score menu program."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell.")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


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