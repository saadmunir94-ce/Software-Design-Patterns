"""

Decorator Method is a Structural Design Pattern which allows you to dynamically
attach new behaviours to objects without changing their implementation by passing
these objects inside wrapper objects that contains the behaviours.

"""
import numpy as np
import pandas as pd
# function decorator to ensure numpy input
# and round off output to 4 decimal places
def ensure_numpy(fn):
    def decorated_function(data):
        print("hello saad")
        # converts input to numpy array
        Array = np.asarray(data)
        # calls fn on input numpy array
        return np.around(fn(Array), 4)
    print("return decorator")
    return decorated_function


@ensure_numpy
def numpysum(Array):
    return Array.sum()
x = np.random.randn(10, 3)
y = pd.DataFrame(x, columns=["A", "B", "C"])
# output of numpy.sum() function
print(f"x.sum(): {x.sum()}")
# output of pandas.sum() function

print(f"y.sum(): {y.sum()}")
# calling decorated numpysum function
print("numpysum(x): ", numpysum(x))
print("numpysum(y): ", numpysum(y))

"""
This is a simple example. But imagine if we define a new function that computes
the standard deviation of elements in an array. We can simply use the same decorator,
and then the function will also accept pandas DataFrame. Hence, all the code to 
polish input is taken out of these functions by depositing them into the decorator. 
This is how we can efficiently reuse the (same) code, i.e., place it inside wrapper.

"""