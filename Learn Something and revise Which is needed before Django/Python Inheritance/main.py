class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language

    def showDetails(self):
        print(
            f"The name of Programmer: {self.id} is {self.name} and he works with {self.language} Language.")


e = Employee("Rohan", 420)
e.showDetails()
p = Programmer("Black", 2, "Python")
p.showDetails()
