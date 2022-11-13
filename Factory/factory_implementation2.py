
class Dummy:
    """
    Static methods in Python are extremely similar to class level methods, the difference is that a static method is bound to a class
    rather than an object. This means that a static method can be called without an object of that class.
    """
    @staticmethod
    def foo():
        print("hello world")
Dummy.foo()
from abc import ABC, abstractmethod
class IProduct(ABC):
    """A Hypothetical class interface (Product)"""
    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method that must be implemented in subclasses"

class ConcreteProductA(IProduct):
    """A Concrete Class that implements the IProduct Interface"""
    def __init__(self):
        self.name = "Product A"
    def create_object(self):
        return self
class ConcreteProductB(IProduct):
    """A Concrete Class that implements the IProduct Interface"""
    def __init__(self):
        self.name = "Product B"
    def create_object(self):
        return self

class ConcreteProductC(IProduct):
    """A Concrete Class that implements the IProduct Interface"""
    def __init__(self):
        self.name = "Product C"
    def create_object(self):
        return self

class Creator:
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product using some business logic"
        if some_property == "a":
            return ConcreteProductA()
        if some_property == "b":
            return ConcreteProductB()
        if some_property == "c":
            return ConcreteProductC()
        return None

# The Client
product = Creator.create_object("b")
print(product.name)