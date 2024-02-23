# #Data Types

# # String
# sTringS = "Hello"
# print(sTringS[0])
# print(sTringS [len(sTringS)-1] )
# print('125' + '25')
# # Wrong print('125' - '25')



# # Integer
# print(125 + 25)
# print(123_123_123) #print(123123123) Are Same

# # float
# 3.14159
# # Boolean 
# True 
# False


# # 2nd Video
# # numChart = len(input("What is your Name?"))
# # numChart = str(numChart) # float()
# # print("Your name has " + numChart + " charecters")
# # print(type(numChart))







# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])
# doAction = num1 + num2
# print(doAction)

# Mathmatical Operation In Python
2+2
7-5
5*5
6/2 # Give a Float type of data
2**3 # next number is the power of the first number 
print( 3 - 3 + 3 / 3 * 3 )




# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = int(weight) / (float(height)**2)
# print(int(bmi))


# # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# ageLeft = 90 - int(age)
# days = ageLeft * 365 
# weeks = ageLeft * 52  
# months = ageLeft * 12
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")




#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# totalBil = float(input("What was the total bill? $"))
# print(totalBil)
# getPercent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# splitPeople = int(input("How many people to split the bill? "))

# divide = round(totalBil * (1 + (getPercent / 100 )) / splitPeople , 2)
# print("Each person should pay: $"+ divide)



# Second Time Try
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = int(int(weight) / (float(height) ** 2))
# print(bmi)



# totalBil = float(input("What was the total bill? $"))
# print(totalBil)
# getPercent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# splitPeople = int(input("How many people to split the bill? "))

# divide = round(totalBil * (1 + (getPercent / 100 )) / splitPeople , 2)
# print("Each person should pay: $"+ divide)


# print("Welcome to the tip calculator!")
# totalBil = float(input("What was the total bill? $"))
# tipParcent = int(input("How much tip would you like to give? 10, 12, or 15? "))
# totalPerson = int(input("How many people to split the bill?"))
# bill = round((totalBil + ((totalBil * tipParcent)/100)) / totalPerson, 2)
# print(f"Each person should pay: ${bill}")

