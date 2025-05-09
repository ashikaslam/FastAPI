'''
🔁 What is reduce() in Python?
reduce() is a function from the functools module in Python used to 
apply a rolling computation to sequential items in an iterable. 
It reduces the iterable to a single cumulative value by applying a specified function
'''

from functools import reduce

# Example 1: Sum of all elements

nums = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, nums)
print("Sum of elements:", sum_result)  # Output: 15

# Example 2: Product of all elements
product_result = reduce(lambda x, y: x * y, nums)
print("Product of elements:", product_result)  # Output: 120

# Example 3: Find the maximum value
nums_with_max = [10, 5, 30, 7, 25]
max_result = reduce(lambda x, y: x if x > y else y, nums_with_max)
print("Maximum value:", max_result)  # Output: 30

# Example 4: Concatenate strings
words = ['Python', 'is', 'awesome']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print("Concatenated sentence:", sentence)  # Output: 'Python is awesome'



'''

💡 When not to use reduce?
In many cases, sum(), max(), or a simple loop might be more readable.
But reduce() shines when you're doing custom accumulations.


'''