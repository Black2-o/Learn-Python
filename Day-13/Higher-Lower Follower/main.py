## Import Here All 
import random
import art
import game_data
from replit import clear



a = random.choice(game_data.data)
b = random.choice(game_data.data)
aFollower = a["follower_count"]
bFollower = b["follower_count"]


def whoIsWon(aFollower, bFollower):
  if aFollower > bFollower:
    return "a"
  elif aFollower < bFollower:
    return "b"


def whoWon(userChose,score,aFollower,bFollower):
  if userChose == whoIsWon(aFollower, bFollower):
    score += 1
    return score
  elif userChose != whoIsWon(aFollower, bFollower):
    return score



def game(score,a,b,aFollower,bFollower):
  userChose = (input("Who has more followers? Type 'A' or 'B': ")).lower()
  score = whoWon(userChose,score,aFollower,bFollower)
  while userChose == whoIsWon(aFollower, bFollower):
    clear()
    if whoIsWon(aFollower, bFollower) == userChose:
  	    print(f"You're right! Current score: {score}")
    a = b
    aFollower = bFollower
    c = random.choice(game_data.data)
    cFollower = c["follower_count"]
    b = c
    bFollower = cFollower
    print(art.logo)
    print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}')
    print(art.vs)
    print(f'Against B:  {b["name"]}, a {b["description"]}, from {b["country"]}')
    userChose = (input("Who has more followers? Type 'A' or 'B': ")).lower()
    score = whoWon(userChose,score,aFollower,bFollower)
  return score
  


#Actual Game Here........
score = 0
print(art.logo)
print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}')
print(art.vs)
print(f'Against B:  {b["name"]}, a {b["description"]}, from {b["country"]}')
x = game(score,a,b,aFollower,bFollower)
print(f"Sorry, that's wrong. Final score: {x}")
print("Code Exit.........")
