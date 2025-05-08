def greet(name):
    """Function to greet the user."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Function to add two numbers."""
    return a + b

if __name__ == "__main__":
    # This block will only execute if the script is run directly
    print("This script is being run directly.")
    
    # Example usage of the functions
    name = input("Enter your name: ")
    print(greet(name))
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is {add_numbers(num1, num2)}.")
else:
    # This block will execute if the script is imported as a module
    print("This script has been imported as a module.")