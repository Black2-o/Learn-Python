#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp





# Start code from Here
with open("./Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines(100)
for name in name_list:
    remove_n_name = name.replace("\n", "")
    final_letter = letter.replace("[name]", f"{remove_n_name}")
    file_directory = f"./Output/letter_for_{remove_n_name}.txt"
    with open(file_directory, mode="w") as final:
        final.write(final_letter)
