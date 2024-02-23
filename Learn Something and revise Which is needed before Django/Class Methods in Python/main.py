class Employee:
    company = "Apple"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(self, newCompany):
        self.company = newCompany


e1 = Employee("Black")
e1.show()
e1.changeCompany("Google")
e1.show()
print(Employee.company)
