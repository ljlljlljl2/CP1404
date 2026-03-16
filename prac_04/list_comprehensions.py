"""CP1404 Practical 04 - List Comprehensions."""

numbers = [1, 4, 9, 16]
squares = [number ** 2 for number in numbers]
print(squares)

usernames = ["jimbo", "giltson98", "bob"]
lengths = [len(username) for username in usernames]
print(lengths)

strings = ["hello", "world", "python", "list"]
upper_strings = [string.upper() for string in strings]
print(upper_strings)

full_names = ["Ada Lovelace", "Alan Turing", "Grace Hopper"]
first_names = [name.split()[0] for name in full_names]
print(first_names)