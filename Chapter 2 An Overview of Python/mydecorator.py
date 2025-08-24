def decorator(func):
    return func()

def hello():
    print('hello')

decorator(hello)