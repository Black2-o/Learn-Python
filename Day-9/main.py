#programming_dictionary = {
#    "Bug":"An error in a program that prevents the program from running as expected.",
#    "Function": "A piece of code that you can easily call over and over again.",
##    "Loop": "The action of doing something over and over again.",
#}
#print(programming_dictionary["Bug"])
#programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)


## Day 9.1 Coding Chellange

#student_scores = {
#    "Harry":81,
#    "Ron": 78,
#    "Hermione" : 99,
#    "Draco":74,
#    "Neville":62,
#}
#Don't change the code above

#ToDo-1: Create an empty dictionary called student_grades.
#student_grades = {}
# 91 -100 Outstanding
# 80 - 90 Grade = Exceeds Expections
# 71 -80 Acceptable
#70 or lower Fail

#ToDo-2: Write your code below to add the grades to student_grades
#for x in student_scores:
#    if student_scores[x] > 90:
#        student_grades[x] = "Outstanding"
#    elif student_scores[x] > 80:
#        student_grades[x] = "Exceeds Expections"
#    elif student_scores[x] > 70:
#        student_grades[x] = "Acceptable"
#    elif student_scores[x] < 71:
#        student_grades[x] = "Fail"
#    

#Don't change the code below
#print(student_grades)



## Day 9.2 Coding Chellange

#travel_log = [
#{
#    "country":"France",
#    "visits":12,
#    "cities":["Paris", "Lille", "Dijon"]
#},
#{
#    "country":"Germany",
#    "visits":5,
#    "cities":["Berlin", "Hamburg", "Stuttgart"]
#},
#]
#
#Do Not change the above
#def add_new_country(country, visits, cities):
#        new_country = {}
#        new_country["country"] = country
#        new_country["visits"] = visits
#        new_country["cities"] = cities
#        travel_log.append(new_country)
##Do Not change the code below
#add_new_country("Russia", 2,["Moscow", "Saint Petersburg"])
#print(travel_log)



# Day 9 Final Project
print("Welcome to the secret auction program.")
everyOnesBidList = []
def objectmake(name, bid):
        objectt = {}
        objectt["name"] = name
        objectt["bid"] = bid
        everyOnesBidList.append(objectt)
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
objectmake(name,bid)
repetOrNotTF = True
while repetOrNotTF != False:
    repetOrNot = input("Are there any other bidders? Type 'yes'or 'no'.")
    if repetOrNot == "yes":
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        objectmake(name,bid)
    elif repetOrNot == "no":
        repetOrNotTF = False
i = 0
emptyList = []
for x in everyOnesBidList:
    emptyList.append(everyOnesBidList[i]["bid"])
    i += 1
maxbid = max(emptyList)
z = 0
for s in everyOnesBidList:
    y = everyOnesBidList[z]["bid"]
    if maxbid == y:
        maxbidName = everyOnesBidList[z]["name"]
    z += 1
print(f"The winner is {maxbidName} with a bid of ${maxbid}.")
