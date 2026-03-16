"""
Emails
Estimate: 20 minutes
Actual:   25 minutes
"""


def main():
    """Store emails and names, then display them."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        default_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

        if confirmation == "" or confirmation == "y":
            name = default_name
        else:
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract a name from an email address."""
    name_part = email.split("@")[0]
    parts = name_part.split(".")
    return " ".join(parts).title()


main()