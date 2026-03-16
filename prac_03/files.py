"""CP1404 Practical 03 - Files."""

# 1. Ask for name and write it to name.txt using open and close
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2. Read name from name.txt and print greeting using open and close
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Read first two numbers from numbers.txt and print their sum using with
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    print(first_number + second_number)

# 4. Read all numbers from numbers.txt and print total using with
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)