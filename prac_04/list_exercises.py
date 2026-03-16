"""CP1404 Practical 04 - List Exercises."""


def main():
    """Run both list exercises."""
    basic_number_operations()
    security_checker()


def basic_number_operations():
    """Prompt for 5 numbers and display statistics."""
    numbers = []

    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def security_checker():
    """Check if username is authorised."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()