"""
Factory Method is a Creational Design Pattern that allows an interface or a class to
create an object, but lets subclasses decide which class or object to instantiate. Using
the Factory Method, we have the best ways to create an object. Here, objects are created without
exposing the logic to the client, and for creating the new type of object, the client
uses the same common interface.
"""


class FrenchLocalizer:
    """ it simply returns the french version """

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg

def Factory(language="English"):
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "Spanish": SpanishLocalizer,
        "English": EnglishLocalizer
    }
    return localizers[language]()

if __name__ == "__main__":
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")
    message = ["car", "bike", "cycle"]
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))