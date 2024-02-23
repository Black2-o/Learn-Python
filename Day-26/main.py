import random
import pandas
# numbers = [1,2,3,4,5]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Black"
# name_letters = [letter for letter in name.upper()]
# print(name_letters)

# new_doubbled_number = [n*2 for n in range(1,5)]
# print(new_doubbled_number)

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# # short_names = [name for name in names if len(name) <= 4]
# # print(short_names)  
# # long_name = [name.upper() for name in names if len(name) >= 5]
# # print(long_name)

# students_score = {student:random.randint(1,100) for student in names}
# print(students_score)
# passed_students = {student:score for (student,score) in students_score.items() if score>= 33}
# print(passed_students)



student_dict = {
    "student":["Angela", "James", "Lily"],
    "score":[56,76,98]
}

#Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
    # print(value)

for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student)
