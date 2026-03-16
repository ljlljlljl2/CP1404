"""
Programming Language class
Estimate: 15 minutes
Actual:   20 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def is_dynamic(self):
        """Return True if language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of programming language."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")