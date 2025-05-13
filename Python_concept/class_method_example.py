"""
This script demonstrates the use of CLASS METHODS in Python.

- Class methods are defined using @classmethod decorator.
- They take `cls` as the first parameter, which refers to the class itself (not an instance).
- Class methods can be used to create factory methods or modify class-level data.
"""

class Person:
    # Class variable
    population = 0

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable
        Person.population += 1

    def show(self):
        print(f"{self.name} is {self.age} years old.")

    @classmethod
    def get_population(cls):
        """Returns the current population count (class-level data)."""
        return cls.population

    @classmethod
    def from_string(cls, person_str):
        """
        Factory method to create a Person instance from a string.
        Example input: "John-25"
        """
        name, age = person_str.split('-')
        return cls(name, int(age))


# Create objects using the regular constructor
p1 = Person("Alice", 30)
p2 = Person("Bob", 28)

# Create object using class method (factory pattern)
p3 = Person.from_string("Charlie-22")

# Show details
p1.show()
p2.show()
p3.show()

# Access class method to get current population
print(f"\nTotal Population: {Person.get_population()}")




'''
✅ Person.population += 1 vs self.population += 1:
Let’s break it down:

🔹 Person.population += 1
This explicitly accesses the class variable population that belongs to the Person class.

All instances of the class share this variable.

It's the correct way to update the shared population count when a new person is created.

🔹 self.population += 1
This first checks if the instance (self) has a variable named population.

If not, Python will:

Read the class variable population,

Increment it,

But assign the new value to self.population, making it an instance variable, not modifying the class variable.

As a result, future calls to Person.population will not reflect this change.


'''
