def decorator(func):
    def wrapper():
        print("before")
        result = func()
        print("after")
        return result
    return wrapper
@decorator
def hello():
    print('hello')

hello()