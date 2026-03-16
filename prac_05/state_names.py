"""CP1404 Practical 05 - State Names."""

CODE_TO_NAME = {
    "ACT": "Australian Capital Territory",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "QLD": "Queensland",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "VIC": "Victoria",
    "WA": "Western Australia"
}


def main():
    """Look up state names from abbreviations."""
    for code, name in CODE_TO_NAME.items():
        print(f"{code:3} is {name}")

    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()


main()