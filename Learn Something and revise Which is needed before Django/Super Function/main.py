class Rectange:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectange):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width


class Cube(Rectange):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


# square = Square(3, 3)
# cube = Cube(3, 3, 3)


# print(square.area())
# print(cube.volume())


class ParentClass:
    def parent_method(self):
        print("This is the parent method.")


class ChildClass(ParentClass):
    # def parent_method(self):
    #     print("BLACK")
    #     super().parent_method()

    def child_method(self):
        print("This is the child method.")
        # super().parent_method()


# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_summary(self):
        return f"Name: {self.name}, ID: {self.id}"


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

    def get_summary(self):
        return f"Name: {self.name}, ID: {self.id}, Language: {self.lang}"


e = Employee("RED", "5690")
p = Programmer("Black", "1150", "Python")
print(e.get_summary())
print(p.get_summary())
