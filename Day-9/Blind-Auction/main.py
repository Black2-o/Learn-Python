from replit import clear
import art
print(art.logo)
print("Welcome to the secret auction program.")
everyOnesBidList = []
def objectmake(name, bid):
        objectt = {}
        objectt["name"] = name
        objectt["bid"] = bid
        everyOnesBidList.append(objectt)
repetOrNotTF = True
repetOrNot = "yes"
while repetOrNotTF != False:
    if repetOrNot == "yes":
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        objectmake(name,bid)
        repetOrNot = input("Are there any other bidders? Type 'yes'or 'no'.")
        clear()
    elif repetOrNot == "no":
        repetOrNotTF = False
i = 0
emptyList = []
for x in everyOnesBidList:
    emptyList.append(everyOnesBidList[i]["bid"])
    i += 1
maxbid = max(emptyList)
z = 0
for s in everyOnesBidList:
    y = everyOnesBidList[z]["bid"]
    if maxbid == y:
        maxbidName = everyOnesBidList[z]["name"]
    z += 1
print(f"The winner is {maxbidName} with a bid of ${maxbid}.")
