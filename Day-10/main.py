# def format_name(f_name , l_name ):
#   """Take a first and last name and format it to return the title case version of the name."""
#   if f_name == "" and l_name == "":
#     return "You didn't provide a valid input"
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result = {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name?"), input("What is your last name?")))


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return "Leap year."
#       else:
#         return "Not leap year."
#     else:
#       return "Leap year."
#   else:
#     return "Not leap year."

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year) == "Leap year.":
#     x = month_days[month - 1]
#     if x == 28:
#       return x + 1
#   else:
#     return month_days[month - 1]
  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True#We Can Use Boolien Data Type True False.Here True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# #   if is_leap(year) == "Leap year.":
# #     x = month_days[month - 1]
# #     if x == 28:
# #       return x + 1
#   if is_leap(year) == True and month == 2:
#       return 29
#   else:
#       return month_days[month - 1]
  
  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)



# Calculator 
from replit import clear
import art
# Add
def add(n1,n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
def calculator():
  print(art.logo)
  repet = True
  userType = "y"
  num1 = float(input("What's the first number?: "))
  while repet != False:
    if userType == "y":
      for symbol in operation:
        print(symbol)
      operation_symbol = input("Pick an operation from the line above: ")
      num2 = float(input("What's the next number?: "))
      function = operation[operation_symbol]
      answer = function(num1 , num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
      userType = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to calculate again Start.:")
      if userType == "y":
        num1 = answer
    elif userType == "n":
      repet = False
      clear()
      calculator()
calculator()
















