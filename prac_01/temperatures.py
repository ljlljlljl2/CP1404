"""
Convert temperatures between Celsius and Fahrenheit.
"""

celsius = float(input("Celsius: "))
fahrenheit = celsius * 9.0 / 5 + 32
print(f"Result: {fahrenheit:.2f} F")

fahrenheit = float(input("Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"Result: {celsius:.2f} C")