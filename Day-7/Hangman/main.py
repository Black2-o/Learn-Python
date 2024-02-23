#from replit import clear
import random
import hangman_art
import hangman_wordlist

stages = hangman_art.stages
word_list = hangman_wordlist.word_list
word_list_meaning = hangman_wordlist.word_list_meaning
chosen_num = random.randint(0, len(word_list)-1)
chosen_word = word_list[chosen_num]#random.choice(word_list)
chosen_word_meaning = word_list_meaning[chosen_num]
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
print("Hangman is a Student based learning program for Bangladesh.\nIt helps Student to learn English Word and It's meaning.")

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(f"The Word is {chosen_word}. This Word Means = {chosen_word_meaning}")

    print(stages[lives])