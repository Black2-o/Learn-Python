import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_in_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
userInput = input("Enter a word: ")
file_is_on = True
while file_is_on:
    try:
        output = [data_in_dict[x] for x in userInput.upper()]
        file_is_on = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        userInput = input("Enter a word: ")

print(output)