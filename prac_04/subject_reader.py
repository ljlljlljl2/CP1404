"""CP1404 Practical 04 - Subject Reader."""

FILENAME = "subject_data.txt"


def main():
    """Load and display subject data."""
    subject_details = load_subject_details(FILENAME)
    display_subject_details(subject_details)


def load_subject_details(filename):
    """Load subject data from file and return as a nested list."""
    subject_details = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            parts[2] = int(parts[2])
            subject_details.append(parts)
    return subject_details


def display_subject_details(subject_details):
    """Display subject details."""
    for subject in subject_details:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()