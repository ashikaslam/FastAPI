"""
Operator Overloading in Python
==============================

What is Operator Overloading?
-----------------------------
In Python, operators such as +, -, *, ==, etc., have default behavior with built-in data types.
However, we can define or "overload" these operators to work with user-defined classes.
This is known as operator overloading.

Why use Operator Overloading?
-----------------------------
- To make custom classes behave like built-in types.
- For more readable and intuitive code.
- For customizing comparison, arithmetic, or representation of objects.

How do we overload operators?
-----------------------------
We use special methods called "Magic Methods" or "Dunder Methods" (Double Underscore Methods).
For example:
- `__add__` → Overloads the `+` operator
- `__eq__`  → Overloads the `==` operator
- `__str__` → Defines string representation for print()

Below is an example of operator overloading with a custom `Point` class.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overload the == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overload the str() function / print()
    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Example Usage:
if __name__ == "__main__":
    p1 = Point(2, 3)
    p2 = Point(4, 5)

    print("Point 1:", p1)  # Calls __str__
    print("Point 2:", p2)

    # Adding two points using overloaded +
    p3 = p1 + p2
    print("Point 3 (p1 + p2):", p3)

    # Check equality using overloaded ==
    print("Is p1 equal to p2?", p1 == p2)
    print("Is p1 equal to Point(2, 3)?", p1 == Point(2, 3))

"""
Expected Output:
----------------
Point 1: Point(2, 3)
Point 2: Point(4, 5)
Point 3 (p1 + p2): Point(6, 8)
Is p1 equal to p2? False
Is p1 equal to Point(2, 3)? True
"""
