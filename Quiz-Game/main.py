from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_data = question_data
question_bank = []
for x in question_data:
    question_text = x["question"]
    question_answer = x["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_no}")