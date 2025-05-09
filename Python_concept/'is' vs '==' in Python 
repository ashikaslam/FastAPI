
# Python: 'is' vs '=='

# 1. Comparing integers (immutable)
a = 1000
b = 1000
print("a == b:", a == b)    # True – same value
print("a is b:", a is b)    # False – different objects in memory (in most cases)

# Small integers (-5 to 256) are cached in Python
x = 100
y = 100
print("x == y:", x == y)    # True
print("x is y:", x is y)    # True – same object due to caching

# 2. Comparing strings (immutable)
str1 = "hello"
str2 = "hello"
print("str1 == str2:", str1 == str2)  # True – same value
print("str1 is str2:", str1 is str2)  # True – may be True due to interning

# 3. Comparing lists (mutable)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list2:", list1 == list2)  # True – same contents
print("list1 is list2:", list1 is list2)  # False – different objects

# 4. Using 'is' to compare to None
x = None
print("x is None:", x is None)  # Recommended

# 5. Comparing custom objects
class MyClass:
    pass

obj1 = MyClass()
obj2 = MyClass()
print("obj1 == obj2:", obj1 == obj2)  # False – default __eq__ doesn't compare attributes
print("obj1 is obj2:", obj1 is obj2)  # False – different objects

obj3 = obj1
print("obj1 is obj3:", obj1 is obj3)  # True – same object