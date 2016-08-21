#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe


class Animal:
    # constructor
    def __init__(self, name):
        # member variable
        self.name = name

    # abstract method. Should be overwritten by child
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print(self.name + " Barks")

dog = Dog("Fifi")
print(dog.name)
dog.make_sound()
