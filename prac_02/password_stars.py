"""Program to get a valid password and print asterisks as long as the password."""

MIN_LENGTH = 8


def main():
    """Get password and print matching asterisks."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password that meets the minimum length requirement."""
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters.")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print asterisks the same length as the password."""
    print("*" * len(password))


main()