# function decorator that calls the function twice
def repeat_decorator(name):
    def decorated_fn(fn):
        print(name)
        fn()
        print(name)
        fn()
        return fn
    # returns a function
    print("lets return decorated function")
    return decorated_fn


# using the decorator on hello_world function
@repeat_decorator("hello")
def hello_world():
    print("Hello world!")

print("bpp")
# call the function
hello_world()

def repeat_decorator(num_repeats=2):
    # repeat decorator should return a function that is a decorator
    def inner_decorator(fn):
        def decorated_fn():
            for i in range(num_repeats):
                fn()
        # return the new function
        return decorated_fn
    # return the decorator that actually takes the function as its input
    return inner_decorator
# use the decorator with num_repeats argument set as 5 to repeat the function call 5 times

@repeat_decorator(2)
def hello_world():
    print("Hello World!")

hello_world()