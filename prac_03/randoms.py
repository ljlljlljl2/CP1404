"""CP1404 Practical 03 - Random numbers."""

import random

# line 1: randint(5, 20) returns an integer from 5 to 20 inclusive.
# Smallest possible: 5
# Largest possible: 20

# line 2: randrange(3, 10, 2) returns one of 3, 5, 7, 9
# Smallest possible: 3
# Largest possible: 9
# Could line 2 have produced a 4? No, because it only counts by 2 from 3.

# line 3: uniform(2.5, 5.5) returns a floating-point number between 2.5 and 5.5
# Smallest possible: 2.5
# Largest possible: 5.5

print(random.randint(5, 20))        # line 1
print(random.randrange(3, 10, 2))   # line 2
print(random.uniform(2.5, 5.5))     # line 3

# Random number between 1 and 100 inclusive
print(random.randint(1, 100))