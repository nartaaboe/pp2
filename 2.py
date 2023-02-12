class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def printname(self):
        print("my name is " + self.name)
p = Person("John", 36)
p.printname()
