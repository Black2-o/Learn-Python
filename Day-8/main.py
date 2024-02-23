#def myFunction():
#    print("Hello")
#    print("World")
#    print("!")
#def greet(name):
#    print(f"Hello {name}")
#    print(f"How are you {name}?")
# greet(input("What is Your Name?"))

#def greet_with(name, location):
#    print(f"How are you {name}")
#    print(f"How tamprature in {location}")
# greet_with("Black", "Boda")
#greet_with(location = "Boda",name = "Black")



# Day 8.1 Coding Challange.
#import math
#def paint_calc(height, width, cover):
#    number_of_cans = math.ceil(((height * width) / cover))
#    print(f"You'll need {number_of_cans} cans of paint.")
#
#
#
## Don't change code below the line
#test_h = int(input("Height of wall: "))
#test_w = int(input("Width of wall: "))
#coverage = 5
#paint_calc(height = test_h, width = test_w, cover= coverage)


##Day 8.2 Coding Challange
##def prime_checker(number):
##    if number == 2 :
##        print("It's a prime number.")
##    elif number == 3 :
##        print("It's a prime number.")
##    elif number == 5 :
##        print("It's a prime number.")
##   elif number == 7 :
##        print("It's a prime number.")
##    elif number % 2 == 0:
##        print("It's not a prime number.")
##    elif number % 3 == 0:
##        print("It's not a prime number.")
##    elif number % 5 == 0:
##        print("It's not a prime number.")
##    elif number % 7 == 0:
##        print("It's not a prime number.")
##    else:
##        print("It's a prime number.")
##Another Way:
#def prime_checker(number):
#    isPrime = True
#    for i in range(2, number):
#        if number % i == 0:
#            isPrime = False
#    if isPrime == True:
#        print("It's a prime number.")
#    else:
#        print("It's not a prime number.")
## Don't change code below the line
#n = int(input("Check this number"))
#prime_checker(number = n)


####  Caesar-cipher-1-start
import math
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

direction = input("Type 'encode' to encrypt, type'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Don't change the code above

# ToDo -1: create a function called 'encrypt' that takes the text and 'shift' as inputs.

def encrypt(x, y):
    encrypted_word = ""
    for text_in in x:
         position = alphabet.index(text_in)
         new_position = position + y
         new_position_next_work = math.floor(new_position / 26)
         if new_position_next_work > 1:
             myltifly = 26 * new_position_next_work
             new_position = new_position - myltifly
         elif new_position_next_work == 1:
             new_position = new_position - 26
         else:
             new_position = new_position
             
         encrypted_letter = alphabet[new_position]
         encrypted_word += encrypted_letter
    print(f"The encoded text is {encrypted_word}")
         
def decrypt(x, y):
    decoded_word = ""
    for text_in in x:
         position = alphabet.index(text_in)
         new_position = position - y             
         decoded_letter = alphabet[new_position]
         decoded_word += decoded_letter
    print(f"The decoded text is {decoded_word}")        

if direction == "encode":
    encrypt(x = text, y = shift)
elif direction == "decode":
    decrypt(x = text, y = shift)

