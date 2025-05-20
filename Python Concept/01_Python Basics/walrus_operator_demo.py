

"""
This Python script explains and demonstrates the use of the "walrus operator"
(introduced in Python 3.8), also known as the assignment expression.
"""

print("-" * 40)
print("Introduction to the Walrus Operator (:=)")
print("-" * 40)

print("""
The walrus operator, denoted by ':=', allows you to assign a value to a
variable as part of an expression. This can make your code more concise
and readable in certain situations by combining assignment and condition
checking.

Before the walrus operator, you would typically have separate lines for
assignment and conditional checks:

  my_variable = some_function()
  if my_variable is not None:
      print(f"The value is: {my_variable}")

With the walrus operator, you can combine these into a single expression:

  if (my_variable := some_function()) is not None:
      print(f"The value is: {my_variable}")

The expression '(my_variable := some_function())' both assigns the result
of 'some_function()' to 'my_variable' and evaluates to the value of
'my_variable' for the 'if' condition.
""")

print("\n" + "-" * 40)
print("Use Cases for the Walrus Operator")
print("-" * 40)

print("""
The walrus operator is particularly useful in the following scenarios:

1.  **Inside Loops:** When you need to perform an action based on a value
    that is also used in the loop condition. This avoids redundant calls
    to the function or expression that produces the value.

2.  **In Conditional Statements:** As shown in the introduction, it can
    simplify conditions where you need to use the assigned value within
    the block.

3.  **List Comprehensions and Generator Expressions:** It can be used to
    include values in the resulting list or generator based on a condition
    that also uses the assigned value.

4.  **Reading Data in Chunks:** When reading data from a file or stream in
    chunks, the walrus operator can make the loop condition more concise.
""")

print("\n" + "-" * 40)
print("Working Example with Output")
print("-" * 40)

import random

def get_random_number_or_none():
    """Returns a random integer between 1 and 10, or None with a 30% chance."""
    if random.random() < 0.3:
        return None
    else:
        return random.randint(1, 10)

print("Demonstrating the walrus operator in a while loop:")
numbers = []
while (number := get_random_number_or_none()) is not None:
    print(f"Generated number: {number}")
    numbers.append(number)

print(f"\nList of generated numbers: {numbers}")

print("\nDemonstrating the walrus operator in a conditional statement:")
if (value := len(numbers)) > 5:
    print(f"The list has {value} elements, which is more than 5.")
else:
    print(f"The list has {value} elements, which is not more than 5.")

print("\n" + "-" * 40)
print("Conclusion")
print("-" * 40)

print("""
The walrus operator provides a concise way to assign values within
expressions, leading to more readable and sometimes more efficient code.
However, it's important to use it judiciously, as overuse can sometimes
make code harder to understand for those not familiar with the operator.
""")