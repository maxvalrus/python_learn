class Person(object):
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

hunter = Person("Max")
print(hunter, hunter.name)
hunter.name = "Test"
print(hunter, hunter.name)
print(hunter, hunter._Person__name)