class Person:
    def __init__(self, person_name: str, dob: int, ht: int = None):
        self.name = person_name
        self.date_of_birth = dob
        self.height = ht

    def get_name(self):
        return self.name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_about(self):
        return f"Name: {self.name}, Date Of Birth: {self.date_of_birth}, Height: {self.height if self.height is not None else 'Invalid'} Feet"

    def set_name(self, new_name):
        self.name = new_name


# a_person = Person("Black", 2007, 5.7)
# b_person = Person("VSCODE", 2012)

# print(a_person.get_about())
# print(b_person.get_about())

# a_person.set_name("Black 2.o")
# print(a_person.get_about())
# print(a_person.name)


person_list = []
person_list.append(Person("Black 2.o", 2007, 6))
person_list.append(Person("Foe", 2003))
person_list.append(Person("Boe", 2006, 5))
person_list.append(Person("KOe", 2008, 4))
person_list.append(Person("Zoo", 2007))
person_list.append(Person("Vee", 2004, 6))
person_list.append(Person("Yas", 2009, ))


# for person in person_list:
#     # print(person.get_date_of_birth())
#     if person.get_date_of_birth() >= 2003:
#         print(person.get_about())


class Student(Person):
    def __init__(self, person_name: str, dob: int, email_id: str, student_id: str, ht: int = None):
        super().__init__(person_name, dob, ht)
        self.id = student_id
        self.email = email_id

    def get_summary(self):
        return f'Name: {self.get_name()}, Email: {self.email}, Birth: {self.get_date_of_birth()}'

    def __str__(self):
        return self.get_summary()
        # return f'Name: {self.get_name()}, Email: {self.email}, Birth: {self.get_date_of_birth()}'


student = Student("A", 2000, "black@gmail.com", "264aga687ga")

# print(student)
# student.set_name("Black")
# print(student)


class Teacher(Person):
    def __init__(self, person_name: str, dob: int, department: str):
        super().__init__(person_name, dob)
        self.department = department

    def get_summary(self):
        return f'Name: {self.get_name()}, Department: {self.department}, Birth: {self.get_date_of_birth()}'

    def __str__(self):
        return self.get_summary()


new_person_list = [
    Person("Black", 1990),
    Student("S", 2007, "s@gmail.com", 'stid'),
    Teacher("T", 2000, "Science")
]
print(new_person_list[0].get_about())
print(new_person_list[1])
print(new_person_list[2])
