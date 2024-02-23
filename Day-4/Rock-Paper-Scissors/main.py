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
    