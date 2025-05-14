"""
Demonstration of Method Overriding in Python.
"""

class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Usage
generic_animal = Animal()
dog = Dog()
cat = Cat()

print("Animal says:", generic_animal.speak())  # Calls Animal's method
print("Dog says:", dog.speak())                # Overridden method in Dog
print("Cat says:", cat.speak())                # Overridden method in Cat
