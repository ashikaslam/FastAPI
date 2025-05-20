# Example of a Lambda Function in Python

# A simple lambda function to add two numbers
add = lambda x, y: x + y

# Using the lambda function
result = add(5, 3)
print(f"The result of addition is: {result}")

# Lambda function to find the square of a number
square = lambda x: x ** 2

# Using the lambda function
num = 4
print(f"The square of {num} is: {square(num)}")

# Lambda function with filter to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Lambda function with map to double the numbers in a list
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled_numbers}")