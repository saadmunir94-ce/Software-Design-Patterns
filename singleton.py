class Person(object):
    def __new__(cls, name):
        print(f"Creating a new {cls.__name__} object")
        obj = object.__new__(cls)
        return obj
    def __init__(self, name):
        print(f"Initializing the person object with {name}")
        self.name = name


class Singleton:
    __instance = None
    def __new__(cls, *args):
        print(cls.__instance)
        if cls.__instance is None:
            print('Creating the singleton object...')
            cls.__instance = super().__new__(cls)
        return cls.__instance


john = Person("John")
singleton = Singleton()
singleton2 = Singleton()
singleton3 = Singleton()
singleton.name = "saad"
print(singleton3.name)