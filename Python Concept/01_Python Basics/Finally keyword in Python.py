
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)











# Demonstrating the use of the 'finally' keyword in Python

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Execution of the 'try-except' block is complete.")

# Test cases
print("Test Case 1:")
divide_numbers(10, 2)

print("\nTest Case 2:")
divide_numbers(10, 0)   