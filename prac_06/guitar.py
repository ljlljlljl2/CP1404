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
        """Return True if guitar is vintage."""
        return self.get_age() >= 50