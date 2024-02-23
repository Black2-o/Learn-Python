class Employee:
    def __init__(self):
        self.__name = "Black"


a = Employee()
# print(a.name)
# print(a.__name)# Cannot Access Directly
print(a._Employee__name)  # But Can Access INdirectly
