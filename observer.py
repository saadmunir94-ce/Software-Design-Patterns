"""
Observer Pattern: In software design and engineering, the observer pattern is a software design pattern in which an object, named the subject,
maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their
methods
"""
class Subject:
    """Represents what is being observed"""
    def __init__(self):
        """creates an empty observer list"""
        self._observers = []
    def notify(self, modifier = None):
        """Alerts the observers"""
        for observer in self._observers:
            if modifier != observer:
                # The subject notifies the observer by calling the update method of the observer with the subject being passed as an argument.
                observer.update(self)

    def attach(self, observer):
        """If the observer is not in the list, append it into the list"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove the observer from the observer list"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class Data(Subject):
    """Monitor the Publisher"""
    def __init__(self, name=""):
        Subject.__init__(self)
        self.name = name # public variable
        self.__data = 0 # private variable

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, val):
        self.__data = val
        self.notify()

class HexViewer:
    """Update the Hexviewer subscriber"""
    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))


class OctalViewer:
    """Update the Octal viewer subscriber"""
    def update(self, subject):
        print('OctalViewer: Subject ' + str(subject.name) + ' has data ' + str(oct(subject.data)))


class DecimalViewer:
    """updates the Decimal viewer subscriber"""

    def update(self, subject):
        print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))
print(__name__)
if __name__ == "__main__":
    print("hello")
    obj1 = Data("Data1")
    obj2 = Data("Data2")

    view1 = DecimalViewer()
    view2 = HexViewer()
    view3 = OctalViewer()

    obj1.attach(view1)
    obj1.attach(view2)
    obj1.attach(view3)

    obj2.attach(view1)
    obj2.attach(view2)
    obj2.attach(view3)

    obj1.data = 15
    obj2.data = 20

