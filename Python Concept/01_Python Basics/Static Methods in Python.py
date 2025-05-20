"""
This file demonstrates how to use static methods in Python.

Static methods:
- Don't receive the `self` (instance) or `cls` (class) arguments.
- Behave like regular functions, but live in the class's namespace.
- Are useful when you want to group utility functions with a class for organization, 
  even if those functions don’t access class or instance data.
"""

from datetime import datetime

class Utility:
    # Static method: general-purpose utility that doesn't need access to instance or class data
    @staticmethod
    def format_date(date_obj, format="%Y-%m-%d"):
        """Format a datetime object into a string."""
        return date_obj.strftime(format)

    @staticmethod
    def is_valid_email(email):
        """Simple check for email validation."""
        return "@" in email and "." in email

    @staticmethod
    def calculate_discount(price, percent):
        """Calculate discount on a product."""
        return price - (price * percent / 100)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.created_at = datetime.now()

    def show_summary(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print("Created:", Utility.format_date(self.created_at))

        if Utility.calculate_discount(self.price, 10) < self.price:
            print("10% discount available!")

# Class method for tracking instances (example for comparison)
class User:
    user_count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        if Utility.is_valid_email(email):
            User.user_count += 1

    @classmethod
    def total_users(cls):
        return cls.user_count

# -------------------------- USAGE EXAMPLES ----------------------------

# Using static methods directly
print("Formatted date:", Utility.format_date(datetime(2025, 5, 12)))
print("Is valid email:", Utility.is_valid_email("user@example.com"))
print("Discounted price:", Utility.calculate_discount(200, 15))

# Using static methods inside other class
p = Product("Laptop", 1200)
p.show_summary()

# Creating users and counting
u1 = User("Alice", "alice@mail.com")
u2 = User("Bob", "bobmail.com")  # Invalid email
u3 = User("Charlie", "charlie@example.com")

print("Total valid users registered:", User.total_users())
