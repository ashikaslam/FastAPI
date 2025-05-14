"""
Demonstration of the super() keyword in Python.
"""

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal initialized with name: {self.name}")

    def speak(self):
        print(f"{self.name} makes a sound.")

# Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent constructor using super()
        super().__init__(name)
        self.breed = breed
        print(f"Dog initialized with breed: {self.breed}")

    def speak(self):
        super().speak()  # Call the parent class speak method
        print(f"{self.name} barks.")

# Usage
d = Dog("Buddy", "Golden Retriever")
d.speak()
