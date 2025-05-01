# Example demonstrating the difference
my_dict = {"name": "Aslam", "age": 25}

# Using dict[key]
try:
    print(my_dict["name"])  # Output: Aslam
    print(my_dict["address"])  # Raises KeyError
except KeyError as e:
    print(f"KeyError: {e}")

# Using dict.get(key)
print(my_dict.get("name"))  # Output: Aslam
print(my_dict.get("address"))  # Output: None
print(my_dict.get("address", "Not Found"))  # Output: Not Found