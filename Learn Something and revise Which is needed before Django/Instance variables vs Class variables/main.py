class Employee:
    company_name = "APPLE"
    noOfEmployee = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee += 1

    def showDetails(self):
        print(
            f"The name of the Employee is {self.name} and the raise amount in {self.company_name} is {self.raise_amount}")


emp1 = Employee("Black")
emp1.raise_amount = 0.2
emp1.company_name = "Apple India"

Employee.company_name = "GOOGLE"
print(Employee.company_name)

emp2 = Employee("ROhan")
emp1.showDetails()

emp2.showDetails()
# Employee.showDetails(emp1)
print(Employee.noOfEmployee)
