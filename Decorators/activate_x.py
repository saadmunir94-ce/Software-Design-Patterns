import numpy as np
from activation import activate
# create a random matrix
x = np.random.randn(5, 3)
print(x)
# try ReLU activation on the matrix
relu_x = activate(x, "relu")
print(relu_x)
# load the functions, and call ReLU again
import funcs
relu_x = activate(x, "relu")
print("Output: ", relu_x)