import math
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

direction = input("Type 'encode' to encrypt, type'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(x, y, z):
    caesar_word = ""      
    for text_in in x:
        position = alphabet.index(text_in)
        if z == "encode":
            new_position = position + y
            new_position_next_work = math.floor(new_position / 26)
        elif z == "decode":
            new_position = position - y
            new_position_next_work = math.floor((new_position * -1)/ 26)
        if new_position_next_work > 1:
            myltifly = 26 * new_position_next_work
            if z == "encode":
                    new_position = new_position - myltifly
            elif z == "decode":
                    new_position = new_position + myltifly
        elif new_position_next_work == 1:
            if z == "encode":
                    new_position = new_position - 26
            elif z == "decode":
                    new_position = new_position + 26
        else:
            new_position = new_position
                    
        caesar_letter = alphabet[new_position]
        caesar_word += caesar_letter
    if z == "encode":
        print(f"The encoded text is {caesar_word}")
    elif z == "decode":
        print(f"The decoded text is {caesar_word}")
        
        
caesar(x = text, y = shift, z = direction)
