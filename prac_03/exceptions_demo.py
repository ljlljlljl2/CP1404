"""CP1404 Practical 03 - Exceptions demo."""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


# Questions:
# When will a ValueError occur?
# A ValueError will occur when the user enters something that cannot be converted to an int.

# When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur when the denominator is 0.

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes. Check that the denominator is not 0 before dividing, and re-prompt if needed.