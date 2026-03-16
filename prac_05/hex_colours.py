"""CP1404 Practical 05 - Hex Colours."""

NAME_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blue": "#0000ff",
    "brown": "#a52a2a"
}


def main():
    """Look up hex colour codes."""
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        try:
            print(f"{colour_name} is {NAME_TO_HEX[colour_name]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower()


main()