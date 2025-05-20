"""
Title: Understanding dir(), __dict__, and help() in Python

Description:
----------------------------------------------------------
In Python, `dir()`, `__dict__`, and `help()` are built-in tools
that help inspect and explore objects, especially useful during
debugging and learning.

1. dir(object)
   - Returns a list of all valid attributes and methods of the object.
   - Helps understand what you can do with an object.

2. __dict__
   - Returns the object's attribute dictionary.
   - Shows internal state, i.e., instance variables and their values.

3. help(object)
   - Launches the built-in help system.
   - Displays the documentation for an object (class, function, module, etc.).
"""

# A sample class to demonstrate all three tools
class Animal:
    species = "Mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says hello!"

# Create an object
dog = Animal("Buddy", 5)

# Using dir()
print("📘 dir(dog):")
print(dir(dog))
print("\n" + "-"*50 + "\n")

# Using __dict__
print("📗 dog.__dict__:")
print(dog.__dict__)  # Shows {'name': 'Buddy', 'age': 5}
print("\n" + "-"*50 + "\n")

# Using help()
print("📙 help(Animal):")
help(Animal)  # Displays the class docstring, methods, and attributes
