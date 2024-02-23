#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password1 = []
for z in range(1, (nr_letters+1)):
  random_num = random.randint(0, (len(letters)-1))
  y = 0
  for x in letters:
    y += 1
    if random_num == y:
      # print(str(x))
      password1.append(x)
# password = "".join(password1)
# print(password)
password2 = []
for z in range(1, (nr_numbers+1)):
  random_num = random.randint(0, (len(numbers)-1))
  y = 0
  for x in numbers:
    y += 1
    if random_num == y:
      # print(str(x))
      password2.append(x)

password3 = []
for z in range(1, (nr_symbols+1)):
  random_num = random.randint(0, (len(symbols)-1))
  y = 0
  for x in symbols:
    y += 1
    if random_num == y:
      # print(str(x))
      password3.append(x)


password_easy = password1 + password2 + password3
# print(password_easy)
asd = random.sample(password_easy, len(password_easy))
# print(asd)
password = "".join(asd)
print(password)
# print(password1)
# print(password2)
# print(password3)