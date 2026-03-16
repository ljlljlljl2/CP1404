"""CP1404 Practical 03 - Exceptions to complete."""

finished = False
result = 0

while not finished:
    try:
        number = int(input("Enter an integer: "))
        result = number * 2
        finished = True
    except ValueError:
        print("Please enter a valid integer.")

print(f"Valid result is {result}")