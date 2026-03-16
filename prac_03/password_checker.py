"""CP1404 Practical 03 - Password Checker."""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Get and validate password."""
    print("Please enter a valid password")
    print_password_requirements()

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print(f"Your {len(password)} character password is valid: {password}")


def print_password_requirements():
    """Print the password rules based on constants."""
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("    1 or more uppercase characters")
    print("    1 or more lowercase characters")
    print("    1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"    and 1 or more special characters:  {SPECIAL_CHARACTERS}")


def is_valid_password(password):
    """Return True if password matches all requirements."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_count = 0

    for character in password:
        if character.islower():
            lowercase_count += 1
        elif character.isupper():
            uppercase_count += 1
        elif character.isdigit():
            digit_count += 1
        elif character in SPECIAL_CHARACTERS:
            special_count += 1

    if lowercase_count < 1:
        return False
    if uppercase_count < 1:
        return False
    if digit_count < 1:
        return False
    if SPECIAL_CHARS_REQUIRED and special_count < 1:
        return False

    return True


main()