def decorator(func):
    def wrapper():
        print("before")
        result = func()
        print("after")
        return result
    return wrapper()

def hello():
    print('hello')

decorator(hello)