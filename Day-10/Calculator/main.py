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