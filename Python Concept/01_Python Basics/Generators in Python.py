"""
Generators in Python
---------------------

A generator in Python is a special type of iterator that allows you to iterate through a sequence of values,
but unlike regular functions, it uses `yield` to return values one at a time, pausing and resuming as needed.

Generators are memory-efficient because they do not store the entire sequence in memory.
They compute and return items only when requested.

Key Features:
- Uses `yield` instead of `return`
- Maintains state between calls
- Can be iterated only once

Use Cases:
- Processing large datasets (e.g., reading large files line by line)
- Generating infinite sequences
- Memory-efficient computations
"""

# Example 1: Basic Generator Function
def count_up_to(max_value):
    print("Generator started")
    count = 1
    while count <= max_value:
        yield count
        count += 1

# Example 2: Generator Expression (like list comprehension, but lazy)
squares = (x*x for x in range(5))  # This is a generator expression

# Example 3: Using generator to read large files line by line (simulation)
def simulate_large_file():
    for i in range(1, 6):
        yield f"Line {i}"

# Main demonstration
if __name__ == "__main__":
    print("Example 1: Using a generator function to count:")
    for num in count_up_to(5):
        print(num)

    print("\nExample 2: Generator expression for squares:")
    for square in squares:
        print(square)

    print("\nExample 3: Simulating reading a large file line-by-line:")
    for line in simulate_large_file():
        print(line)

"""
Expected Output:

Example 1: Using a generator function to count:
Generator started
1
2
3
4
5

Example 2: Generator expression for squares:
0
1
4
9
16

Example 3: Simulating reading a large file line-by-line:
Line 1
Line 2
Line 3
Line 4
Line 5
"""
