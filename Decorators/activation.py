# activation.py
ACTIVATION = {}

def register(name):
    def decorator(fn):
        #print("running decorator")
        # assign fn to "name" key in ACTIVATION
        #print(f"name is {fn}")
        ACTIVATION[name] = fn
        # return fn unmodified
        return fn
    #print("returning decorator")
    return decorator
def activate(x, kind):
    try:
        fn = ACTIVATION[kind]
        print(fn)
        return fn(x)
    except KeyError:
        print(f"Activation function {kind} undefined.")
