"""
Function Caching in Python:
---------------------------
Function caching is a technique to store the results of expensive function calls
and reuse them when the same inputs occur again. This can drastically improve
performance for functions that are called repeatedly with the same arguments.

In Python, this is typically done using the `functools.lru_cache` decorator.

Use cases:
- Recursion-heavy problems like calculating Fibonacci numbers.
- Expensive computations where the same input appears multiple times.
- API calls or database lookups where results can be reused.

Class Methods in Python:
------------------------
A class method is a method that is bound to the class and not the instance.
It takes `cls` as the first parameter instead of `self`.

Use cases:
- Factory methods that return class instances.
- Accessing or modifying class-level state.
"""

import time
from functools import lru_cache

# --------------------------------------------
# Function Caching Demo
# --------------------------------------------

@lru_cache(maxsize=None)  # Unlimited caching
def slow_fibonacci(n):
    """Return the nth Fibonacci number (slow version with caching)."""
    if n < 2:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


def demo_function_caching():
    print("Calculating Fibonacci numbers with function caching (lru_cache)...")
    start = time.time()
    print("Fibonacci(35):", slow_fibonacci(35))  # Expensive the first time
    end = time.time()
    print("Time taken first call: {:.2f} seconds".format(end - start))

    start = time.time()
    print("Fibonacci(35) again:", slow_fibonacci(35))  # Fast from cache
    end = time.time()
    print("Time taken second call: {:.6f} seconds".format(end - start))


# --------------------------------------------
# Class Method Demo
# --------------------------------------------

class Circle:
    PI = 3.1416

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        """Alternative constructor using class method."""
        radius = diameter / 2
        return cls(radius)


def demo_class_method():
    print("\nCreating Circle using class method...")
    c = Circle.from_diameter(10)
    print("Radius:", c.radius)
    print("Area:", c.area())


# --------------------------------------------
# Run the demos
# --------------------------------------------

if __name__ == "__main__":
    demo_function_caching()
    demo_class_method()
