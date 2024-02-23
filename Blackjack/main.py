############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run




# ## Start From Here
import art
import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]#13
firstYourChosenCard = random.choice(cards)
secondYourChosenCard = cards[random.randint(0, 12)]

yourTotal = firstYourChosenCard + secondYourChosenCard

computerChosenCardFirst = random.choice(cards)
computerChosenCardSecond = random.choice(cards)
comTotal = computerChosenCardFirst + computerChosenCardSecond
if comTotal < 15:
  while comTotal > 15:
    computerChosenCardNext = random.choice(cards)
    comTotal += computerChosenCardNext
yourChosenCard = [firstYourChosenCard, secondYourChosenCard]
comChosenCard = [computerChosenCardFirst, computerChosenCardSecond]
playNow = True
while playNow != False:
  playOrNot = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  clear()
  if playOrNot == "y":
    print(art.logo)
    print(f"    Your cards: {yourChosenCard}, current score: {yourTotal}")
    print(f"    Computer's first card: {computerChosenCardFirst}")
    againOrNots = True
    againOrNot = input("Type 'y' to get another card, type 'n' to pass: ")

    while againOrNots != False:
      if againOrNot == "y":
        nextYourChosenCard = random.choice(cards)
        yourChosenCard.append(nextYourChosenCard)
        yourTotal += nextYourChosenCard
        print(f"    Your cards: {yourChosenCard}, current score: {yourTotal}")
        print(f"    Computer's first card: {computerChosenCardFirst}")
        if yourTotal > 21:
          againOrNots = False
          print("You went over. You lose 😤") 
        elif comTotal < 15:
          while comTotal < 15:
            computerChosenCardNext = random.choice(cards)
            comTotal += computerChosenCardNext
            comChosenCard.append(computerChosenCardNext)
        elif comTotal > 21:
          print("Oponent went over. You win 😁")
        else:
          againOrNot = input("Type 'y' to get another card, type 'n' to pass: ")

      elif againOrNot == "n":
        print(f"Your final hand: {yourChosenCard}, final score: {yourTotal}")
        print(f"Computer's final hand: {comChosenCard}, final score: {comTotal}")
        againOrNots = False
        if comTotal > yourTotal:
            print("You lose.")
            againOrNots = False
        elif  comTotal < yourTotal:
            print("You Won.")
            againOrNots = False
  elif playOrNot == "n":
    print("Code Exit.......")
    playNow = False