"""CP1404 Practical 07 - Language File Reader."""

from programming_language import ProgrammingLanguage

FILENAME = "languages.csv"


def main():
    """Read languages from file and display them."""
    languages = load_languages(FILENAME)
    for language in languages:
        print(language)


def load_languages(filename):
    """Load programming languages from CSV file."""
    languages = []
    in_file = open(filename, "r")
    in_file.readline()  # Skip header

    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0]
        typing = parts[1]
        reflection = parts[2] == "Yes"
        year = int(parts[3])
        pointer_arithmetic = parts[4] == "Yes"
        language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
        languages.append(language)

    in_file.close()
    return languages


main()