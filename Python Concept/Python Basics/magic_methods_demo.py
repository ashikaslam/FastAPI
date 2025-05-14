"""
magic_methods_demo.py

This script explains and demonstrates Magic Methods (also called Dunder Methods) in Python.

What are Magic Methods?
------------------------
Magic methods are special methods that start and end with double underscores (__) and allow us to define or customize the behavior of objects.

Why use Magic Methods?
-----------------------
They let our custom classes behave like built-in Python types. For example:
- Use `+` to add objects
- Use `len()` to get size
- Print objects cleanly with `str()`
- Compare objects with `==`

This makes our classes more intuitive and Pythonic.

Below is an example using a `Book` class with several magic methods.
"""

class Book:
    def __init__(self, title, pages):
        """Called when creating a new instance."""
        self.title = title
        self.pages = pages

    def __str__(self):
        """Called by str(), or when printing an object."""
        return f"'{self.title}' with {self.pages} pages"

    def __repr__(self):
        """Called by repr(), used in debugging or development."""
        return f"Book(title={self.title}, pages={self.pages})"

    def __len__(self):
        """Called by len(). Returns number of pages."""
        return self.pages

    def __add__(self, other):
        """Defines behavior for `book1 + book2`."""
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

    def __eq__(self, other):
        """Defines behavior for `book1 == book2`."""
        return self.pages == other.pages

# Example usage
book1 = Book("Python Basics", 300)
book2 = Book("Advanced Python", 200)

print("STR:", str(book1))         # __str__
print("REPR:", repr(book2))       # __repr__
print("LEN:", len(book1))         # __len__
print("ADD:", book1 + book2)      # __add__
print("EQUAL:", book1 == book2)   # __eq__
