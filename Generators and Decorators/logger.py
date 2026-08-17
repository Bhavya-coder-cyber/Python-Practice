from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@logger
def brew(type, milk = "no"):
    print(f"Brewing {type} and {milk} milk")

brew("green tea")


    