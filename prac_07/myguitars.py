"""
My Guitars
Estimate: 30 minutes
Actual:   40 minutes
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load, display, sort, add, and save guitars."""
    guitars = load_guitars(FILENAME)

    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nThese are my guitars sorted by year:")
    display_guitars(guitars)

    add_new_guitars(guitars)
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from file."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, start=1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def add_new_guitars(guitars):
    """Ask user for new guitars and add them to list."""
    print("\nMy guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Save guitars to file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()