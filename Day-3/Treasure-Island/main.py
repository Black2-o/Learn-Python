print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
import random
whichSideGoNumber = random.randint(1, 2)
whichSideGo = (input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right" \n'
)).lower()

if whichSideGoNumber == 1:
    howToGoNum = random.randint(1, 2)
    howToGo = (input(
        'You come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "swim" to swim across. \n'
    )).lower()
    if howToGoNum == 2:
        whichRoomGoNum = random.randint(1, 3)
        whichRoomGo = (input(
            'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose  \n'
        )).lower()
        if whichRoomGoNum == 1:
            print("It's a room full of fire. Game Over")
        elif whichRoomGoNum == 2:
            print('You found the treasure! You Win!')
        elif whichRoomGoNum == 3:
            print('You enter a room of beasts. Game Over.')

    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")

