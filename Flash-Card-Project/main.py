# Import 
from tkinter import *
import pandas
import random
#Constant 
BACKGROUND_COLOR = "#B1DDC6"




# Improt Data From Pandas
try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("data/french_words.csv")
word_data_in_dict = word_data.to_dict(orient="records")

# print(word_data_in_dict)


# Word Change By Random


def random_word():
    global timer
    window.after_cancel(timer)
    global word
    word = random.choice(word_data_in_dict)
    word_french = word["French"]
    canvas.itemconfig(image, image=bg_front_image)
    canvas.itemconfig(title_text, fill="black", text="French")
    canvas.itemconfig(word_text, fill="black", text=f"{word_french}")
    timer = window.after(3000, random_word_meaning)





def random_word_meaning():
    meaning = word["English"]
    canvas.itemconfig(image, image=bg_back_image)
    canvas.itemconfig(title_text, fill="white",text="English")
    canvas.itemconfig(word_text, fill="white",text=f"{meaning}")





def is_known():
    word_data_in_dict.remove(word)
    print(len(word_data_in_dict))
    dataX = pandas.DataFrame(word_data_in_dict)
    dataX.to_csv("data/words_to_learn.csv", index=False)
    random_word()





# Set up UI 
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)

bg_front_image = PhotoImage(file="images/card_front.png")
bg_back_image = PhotoImage(file="images/card_back.png")


image = canvas.create_image(400, 263, image=bg_front_image)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40 , "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60 , "bold"))
global timer
timer = window.after(3000, random_word_meaning)
random_word()


right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)
canvas.grid(column=0, row=0, columnspan=2)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)



window.mainloop()
