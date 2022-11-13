# funcs.py
from activation import register
#from activation import ACTIVATION
import numpy as np


@register("relu")
def relu(x):
    return np.where(x > 0, x, 0)

@register("sigmoid")
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

@register("tanh")
def tanh(x):
    return np.tanh(x)

#print(ACTIVATION)
