"""
This Python script demonstrates the difference between:
- Class Variables: Shared among all instances.
- Instance Variables: Unique to each instance.
"""

class Car:
    # Class variable (shared across all instances)
    wheels = 4

    def __init__(self, color):
        # Instance variable (unique to each object)
        self.color = color


# Create two Car objects
car1 = Car("Red")
car2 = Car("Blue")

# Show initial state
print("Initial values:")
print(f"car1 - Color: {car1.color}, Wheels: {car1.wheels}")
print(f"car2 - Color: {car2.color}, Wheels: {car2.wheels}")

# Change the class variable using the class name
Car.wheels = 6

print("\nAfter modifying class variable through class:")
print(f"car1 - Color: {car1.color}, Wheels: {car1.wheels}")
print(f"car2 - Color: {car2.color}, Wheels: {car2.wheels}")

# Override the class variable only for car1 instance
car1.wheels = 8

print("\nAfter overriding wheels in car1 instance only:")
print(f"car1 - Color: {car1.color}, Wheels: {car1.wheels}")  # 8 (instance-specific)
print(f"car2 - Color: {car2.color}, Wheels: {car2.wheels}")  # 6 (still shared)
