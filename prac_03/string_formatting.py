"""CP1404 Practical 03 - String Formatting."""

# Walkthrough example values
price = 16035.9
year = 1922
model = "Gibson L-5 CES"

# Required output
print(f"{year} {model} for about ${price:,.0f}!")

# Powers of 2
for i in range(11):
    print(f"2 ^{i:>2} is {2 ** i:>4}")