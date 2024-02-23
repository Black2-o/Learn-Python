from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = self.quiz.score
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)



        # Create Score 
        self.text = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 14, "normal"))
        self.text.grid(column=1, row=0, pady=10)

        # Canvas Created 
        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,width=280, text="HELLO World", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        # Button Created
        self.right_button_image = PhotoImage(file ="images/true.png")
        self.right_button = Button(image=self.right_button_image, highlightthickness=0, command=self.check_true)
        self.right_button.grid(column=0, row=2)
        self.wrong_button_image = PhotoImage(file ="images/false.png")
        self.wrong_button = Button(image=self.wrong_button_image, highlightthickness=0, command=self.check_false)
        self.wrong_button.grid(column=1, row=2)
        
        self.get_next_question()

        self.window.mainloop()

    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of Quiz. Your final Score is {self.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_true(self):
        ans = "True"
        self.check(ans)
        
    def check_false(self):
        ans = "False"
        self.check(ans)

    def check(self, ans):
        x = self.quiz.check_answer(ans)      
        if x == True:
            self.score +=1
            self.text.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)