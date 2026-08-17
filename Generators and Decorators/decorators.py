from functools import wraps
def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorators
def my_function():
    print("Inside function")

my_function()
print(my_function.__name__)