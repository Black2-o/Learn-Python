# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120 :
#   print("You can ride the rollercoaster")
#   age = int(input("What is your Age?"))
#   if age >= 18:
#     print("Adult tickets are $12.")
#     bill = 12
#   elif age  > 12 :
#     print("Youth tickets are $7.")
#     bill = 7
#   elif age >= 45 and age <= 55:
#     print("Everything is ok. Have a free ride with us.")
#   else:
#     print("Childs tickets are $5.")
#     bill = 5
#   wantsPhotos = input("Do You want to a photo taken? Y or N. ")
#   if wantsPhotos == "Y":
#     bill+=3
#   else:
#     bill = bill
#   print(f"Your total bill is ${bill}")
# else:
#   print(f"Sorry, you have to grow {120 - height} cm tall before you can ride")

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# f"Your BMI is 28, you are slightly overweight."
# f"Your BMI is 33, you are obese."
# f"Your BMI is 40, you are clinically obese."

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = round(weight / (height**2))

# if bmi <= 18 :
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi <= 22:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi <= 28:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi <= 33:
#   print(f"Your BMI is {bmi}, you are obese.")
# elif bmi <= 40:
#   print(f"Your BMI is {bmi}, you are clinically obese.")
# else:
#   print("Are You still Alive.")

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if year % 4 == 0:
#     print("Leap year.")
#     if year % 100 == 0:
#         print("Not leap year.")
#     elif year % 400 == 0:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bill = 0
# if size == "S":
#     bill+=15
#     if add_pepperoni == "Y":
#         bill+=2
# elif size == "M":
#     bill+=20
#     if add_pepperoni == "Y":
#         bill+=3
# elif size == "L":
#     bill+=25
#     if add_pepperoni == "Y":
#         bill+=3
# if extra_cheese == "Y":
#     bill+=1
# print(f"Your final bill is: ${bill}")

# # #Love Calculator
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1 = name1.lower()
# name2 = name2.lower()
# name = name1 + name2
# t = name.count("t")
# r = name.count("r")
# u = name.count("u")
# e = name.count("e")
# leftScore = str(t + r + u + e)
# l = name.count("l")
# o = name.count("o")
# v = name.count("v")
# rightScore = str(l + o + v + e)
# score = int(leftScore + rightScore)

# if score < 10 or score > 90 :
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif score <= 50 or score >= 40 :
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
#

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# #Write your code below this line 👇

# whichSideGo = (input(
#     'You\'re at a cross road. Where do you want to go? Type "left" or "right" \n'
# )).lower()

# if whichSideGo == "left":
#     howToGo = (input(
#         'You come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "swim" to swim across. \n'
#     )).lower()
#     if howToGo == "wait":
#         whichRoomGo = (input(
#             'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose  \n'
#         )).lower()
#         if whichRoomGo == "red":
#             print("It's a room full of fire. Game Over")
#         elif whichRoomGo == "yellow":
#             print('You found the treasure! You Win!')
#         elif whichRoomGo == "blue":
#             print('You enter a room of beasts. Game Over.')

#     else:
#         print("You get attacked by an angry trout. Game Over.")

# else:
#     print("You fell into a hole. Game Over.")



