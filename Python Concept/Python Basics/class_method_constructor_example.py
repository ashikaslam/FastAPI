"""
Title: Class Methods as Alternative Constructors in Python

Description:
----------------------------------------------------------
In Python, a class method is a method that is bound to the class
and not the instance of the object. It takes `cls` as the first
argument, which refers to the class itself.

Class methods are defined using the @classmethod decorator.

✅ Use Cases:
----------------------------------------------------------
- Accessing or modifying class state.
- Creating alternative constructors — these are special class methods
  that return an instance of the class using different parameters or formats.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} is {self.age} years old.")

    @classmethod
    def from_string(cls, info_str):
        """
        Alternative constructor that creates a Person object from a string.
        Example input: "Alice-30"
        """
        name, age = info_str.split('-')
        return cls(name, int(age))

    @classmethod
    def from_dict(cls, info_dict):
        """
        Alternative constructor that creates a Person object from a dictionary.
        Example input: {"name": "Bob", "age": 25}
        """
        return cls(info_dict['name'], info_dict['age'])


# Creating instances using the regular constructor
p1 = Person("John", 40)

# Creating instances using alternative constructors
p2 = Person.from_string("Alice-30")
p3 = Person.from_dict({"name": "Bob", "age": 25})

# Displaying all persons
print("Displaying people created with various constructors:\n")
p1.display()
p2.display()
p3.display()
