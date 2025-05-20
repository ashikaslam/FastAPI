# Definition of a Decorator in Python:
# A decorator in Python is a design pattern that allows you to modify the behavior of a function or a class method.
# It is typically used to wrap another function in order to extend its behavior without permanently modifying it.




#Example of a decorator 
def my_decorator(func):
    def wrapper():
        print("befrore the func is called")
        func()
        print("after the func is called")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
# Using the decorated function
say_hello()



my_decorator(say_hello)() #manually calling the decorator