import art
import random
from replit import clear


def winOrNot(attempts, make_a_guess):
  if attempts == 1 and make_a_guess != computer_gussed:
    print("You've run out of guesses, you lose.")
    
def guess_checking(attempts, make_a_guess):
    if make_a_guess > computer_gussed and attempts != 0:
      return "Too high."
    elif make_a_guess < computer_gussed and attempts != 0:
      return "Too low."

def game(computer_gussed,level):
  if level == "easy":
    attempts = 11
  elif level == "hard":
    attempts = 6
  make_a_guess = 0
  while attempts != 1:
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
    make_a_guess = int(input("Make a guess: "))
    print(guess_checking(attempts, make_a_guess))
    if attempts > 1 and make_a_guess != computer_gussed:
      print("Guess Again.")
    winOrNot(attempts, make_a_guess)
    if make_a_guess == computer_gussed:
      return f"You got it! The answer was {computer_gussed}."





## Game Start Here 
playOrNot = True
while playOrNot != False:
  computer_gussed = random.randint(1 , 100)
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  print(game(computer_gussed,level))
  playOrNots = input("Do You Want To Play Again.Type 'y' for yes or Type 'n' for No.")
  clear()
  if playOrNots == "y":
    playOrNot = True
  else:
    playOrNot = False
    print("Code Exit....")
