"""
Guitar class
Estimate: 20 minutes
Actual:   25 minutes
"""

from datetime import date


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return the age of the guitar."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if guitar is 50 or more years old."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Return True if this guitar is older than the other guitar."""
        return self.year < other.year