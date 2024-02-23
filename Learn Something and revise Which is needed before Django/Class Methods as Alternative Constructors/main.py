class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(self, string):
        return self(details.split("-")[0], int(details.split("-")[1]))


e = Employee("Harry", 120000)
print(e.name)

details = 'Black-20000'
e1 = Employee.fromStr(details)
print(e1.name)
print(e1.salary)
print(type(e1.salary))
