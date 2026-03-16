"""
Programming Language class
Estimate: 15 minutes
Actual:   18 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if language uses dynamic typing."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"