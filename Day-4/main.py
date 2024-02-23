# import random

# random_int = random.randint(1 , 10)
# print(random_int)
# import myModule

# print(myModule.pi)


# random_float = random.random()
# print(random_float)

# random_num = round(random.random() * 5)
# print(random_num)


# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
	 
# #Write the rest of your code below this line 👇
# import random 
# randomNumber = random.randint(1,2)
# if randomNumber == 1:
#   print("Heads")
# else:
#   print("Tails")


# # List in Python In javascript this is call array 
# states_of_america = ["New York" , "Washingtone", "etc etc"]
# states_of_america[1] = "newYork"
# print(states_of_america[0])
# print(states_of_america[-1])
# print(states_of_america)
# states_of_america.append("noLand")
# print(states_of_america)
# states_of_america.extend(["California" , "Texes"])
# print(states_of_america)
#
#https://docs.python.org/3/tutorial/datastructures.html


# #Code Challange 

# # Import the random module here

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# namesLen = len(names) - 1 
# import random
# randomNum = random.randint(0, namesLen)
# randomPerson = names[randomNum]
# #  randomPerson = random.choce(names) // We can use by one line of code by this.
# print(randomPerson +" is going to buy the meal today!" )


# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# position = position.split()
# horizonal = int(position[0]) - 1 
# vertical = int(position[1])  
# selectedRow = map[vertical - 1]
# selectedRow[horizonal] = "X"


# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")








# Days final Project 
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇
# userChosen = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

# import random
# computerChosen = random.randint( 0 , 2)
# if userChosen >= 0 or userChosen <= 2: 
#   if userChosen == 0:
#     print(rock)
#   elif userChosen == 1:
#     print(paper)
#   elif userChosen == 2:
#     print(scissors)
  
#   print("Computer Chose")
#   if computerChosen == 0:
#     print(rock)
#   elif computerChosen == 1:
#     print(paper)
#   elif computerChosen == 2:
#     print(scissors)
  
#   if userChosen == computerChosen :
#     print("It's a draw")
#   elif userChosen > computerChosen:
#     if userChosen == 2 and computerChosen == 0:
#       print("You lose")
#     else:
#       print("You win!")
  
#   if computerChosen > userChosen:
#     if computerChosen == 2 and  userChosen== 0:
#       print("You win!")
#     else:
#       print("You lose")
# else:
#   print("You typed an invalid number, you lose!")





# Days Second time Try

# Import the random module here

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# namesLen = len(names)
# import random
# randomNum = random.randint(1, namesLen)
# randomPerson = names[randomNum - 1]
# print(randomPerson +" is going to buy the meal today!$" )


# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# position = list(position)
# column = int(position[0]) - 1
# row = int(position[1]) - 1
# map[row][column] = "X"



# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
cSelect = random.randint( 0 , 2)
youSelect = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if youSelect == 0:
    print(rock)
elif youSelect == 1:
    print(paper)
elif youSelect == 2:
    print(scissors)
else:
    print("Please select write One.😑")
print("Computer chose:")

if cSelect == 0:
    print(rock)
elif cSelect == 1:
    print(paper)
elif cSelect == 2:
    print(scissors)
else:
    print("Please select write One.😑")

# It's a draw You win! You lose
if youSelect == 2 and cSelect == 0:
    print("You lose")
elif youSelect == 0 and cSelect == 2:
    print("You win!")
elif youSelect > cSelect:
    print("You win!")
elif youSelect == cSelect:
    print("It's a draw")
elif cSelect > youSelect:
    print("You lose")
    