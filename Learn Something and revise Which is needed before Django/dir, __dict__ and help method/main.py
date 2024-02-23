# Dir Method
x = [1, 2, 3]
# print(dir(x))

# print(x.__add__)

y = (1, 2, 3)

# print(dir(y))

# __dict__ method


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


p = Person("Jhon", 25)
# print(p.__dict__)


# Help Method

# print(help(str))
print(help(Person))
