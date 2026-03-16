"""
CP1404/CP5632 Assignment 1 - Travel Tracker 1.0
Name: [Junliang Li]
Started: 02/03/2026
GitHub URL: [https://github.com/ljlljlljl2/CP1404]
"""

import random

MENU = """Menu:
D - Display all places
R - Recommend a random place
A - Add a new place
M - Mark a place as visited
Q - Quit"""

FILENAME = "places.csv"

NAME_INDEX = 0
COUNTRY_INDEX = 1
PRIORITY_INDEX = 2
STATUS_INDEX = 3

UNVISITED = "n"
VISITED = "v"


def main():
    """Run the travel tracker program."""
    print("Travel Tracker 1.0 - by [Your Name]")
    places = load_places(FILENAME)
    print(f"{len(places)} places loaded from {FILENAME}")

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "D":
            display_places(places)
        elif choice == "R":
            recommend_place(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_place_as_visited(places)
        elif choice == "Q":
            save_places(FILENAME, places)
            print(f"{len(places)} places saved to {FILENAME}")
            print("Have a nice day :)")
        else:
            print("Invalid menu choice")


def load_places(filename):
    """Load places from a CSV file into a list of lists."""
    places = []
    in_file = open(filename, "r", encoding="utf-8")
    for line in in_file:
        parts = line.strip().split(",")
        parts[PRIORITY_INDEX] = int(parts[PRIORITY_INDEX])
        places.append(parts)
    in_file.close()
    return places


def save_places(filename, places):
    """Save places to a CSV file."""
    out_file = open(filename, "w", encoding="utf-8")
    for place in places:
        print(f"{place[NAME_INDEX]},{place[COUNTRY_INDEX]},{place[PRIORITY_INDEX]},{place[STATUS_INDEX]}", file=out_file)
    out_file.close()


def display_places(places):
    """Display all places sorted by status and priority."""
    places.sort(key=lambda place: (place[STATUS_INDEX], place[PRIORITY_INDEX]))

    max_name_length = max(len(place[NAME_INDEX]) for place in places)
    max_country_length = max(len(place[COUNTRY_INDEX]) for place in places)

    unvisited_count = 0
    for i, place in enumerate(places, start=1):
        marker = "*"
        if place[STATUS_INDEX] == VISITED:
            marker = " "
        else:
            unvisited_count += 1

        print(f"{marker}{i}. {place[NAME_INDEX]:<{max_name_length}} in {place[COUNTRY_INDEX]:<{max_country_length}} {place[PRIORITY_INDEX]}")

    print(f"{len(places)} places tracked. You still want to visit {unvisited_count} places.")


def recommend_place(places):
    """Recommend a random unvisited place."""
    unvisited_places = []
    for place in places:
        if place[STATUS_INDEX] == UNVISITED:
            unvisited_places.append(place)

    if len(unvisited_places) == 0:
        print("No places left to visit!")
    else:
        recommended_place = random.choice(unvisited_places)
        print("Not sure where to visit next?")
        print(f"How about... {recommended_place[NAME_INDEX]} in {recommended_place[COUNTRY_INDEX]}?")


def add_place(places):
    """Add a new place to the list."""
    name = get_valid_string("Name: ")
    country = get_valid_string("Country: ")
    priority = get_valid_priority("Priority: ")

    new_place = [name, country, priority, UNVISITED]
    places.append(new_place)
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def mark_place_as_visited(places):
    """Mark a selected place as visited."""
    unvisited_count = count_unvisited_places(places)
    if unvisited_count == 0:
        print("No unvisited places")
        return

    display_places(places)
    print("Enter the number of a place to mark as visited")
    place_number = get_valid_place_number(len(places))
    selected_place = places[place_number - 1]

    if selected_place[STATUS_INDEX] == VISITED:
        print(f"You have already visited {selected_place[NAME_INDEX]}")
    else:
        selected_place[STATUS_INDEX] = VISITED
        print(f"{selected_place[NAME_INDEX]} in {selected_place[COUNTRY_INDEX]} visited!")


def get_valid_string(prompt):
    """Get a non-blank string from the user."""
    text = input(prompt).strip()
    while text == "":
        print("Input can not be blank")
        text = input(prompt).strip()
    return text


def get_valid_priority(prompt):
    """Get a valid priority greater than 0."""
    is_valid = False
    while not is_valid:
        try:
            priority = int(input(prompt))
            if priority <= 0:
                print("Number must be > 0")
            else:
                is_valid = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return priority


def get_valid_place_number(maximum):
    """Get a valid place number from the user."""
    is_valid = False
    while not is_valid:
        try:
            number = int(input(">>> "))
            if number <= 0:
                print("Number must be > 0")
            elif number > maximum:
                print("Invalid place number")
            else:
                is_valid = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


def count_unvisited_places(places):
    """Count how many places are still unvisited."""
    count = 0
    for place in places:
        if place[STATUS_INDEX] == UNVISITED:
            count += 1
    return count


main()
