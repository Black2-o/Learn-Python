from turtle import Turtle, Screen
import pandas

turtle = Turtle()
turtle_txt = Turtle()
# Screen Work 
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

ans_state = (screen.textinput(title="Guess the State", prompt="What's another State's name?")).lower()


def ansCapitalize():
    if ans_state =="":
        z = "nothing"
    else:
        ans_in_list = ans_state.split()
        y = ""
        for ans in ans_in_list:
            x = ans.capitalize()
            ansin = y + " " + x
            y = x
            z = ansin
    ans_in_capitalize = z
    if ans_in_capitalize == " " + x:
        ans_in_capitalize = x
    else:
        ans_in_capitalize = z
    return ans_in_capitalize

# import Data 
data = pandas.read_csv("50_states.csv")
data_list = data["state"].to_list()
data_x = data["x"].to_list()
data_y = data["y"].to_list()

score = 0
while score != 2:
    data_ans = ansCapitalize()
    data_added = []
    if data_ans in data_added:
        score += 0
        ans_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's another State's name?")).lower()       
    elif data_ans in data_list:
        data_index = data_list.index(data_ans)

        turtle_txt.hideturtle()
        turtle_txt.penup()

        turtle_txt.goto(data_x[data_index], data_y[data_index])
        turtle_txt.write(f"{data_ans}", move=False, font=("Arial", 8, "normal")) 

        data_added.append(data_ans)

        score += 1
        ans_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's another State's name?")).lower()
    else:
        score += 0
        ans_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's another State's name?")).lower()

turtle_txt.write("You Won", move=False, font=("Arial", 24, "normal")) 
screen.mainloop()










# {'state': {0: 'Alabama', 1: 'Alaska', 2: 'Arizona', 3: 'Arkansas', 4: 'California', 5: 'Colorado', 6: 'Connecticut', 7: 'Delaware', 8: 'Florida', 9: 'Georgia', 10: 'Hawaii', 11: 'Idaho', 12: 'Illinois', 13: 'Indiana', 14: 'Iowa', 15: 'Kansas', 16: 'Kentucky', 17: 'Louisiana', 18: 'Maine', 19: 'Maryland', 20: 'Massachusetts', 21: 'Michigan', 22: 'Minnesota', 23: 'Mississippi', 24: 'Missouri', 25: 'Montana', 26: 'Nebraska', 27: 'Nevada', 28: 'New Hampshire', 29: 'New Jersey', 30: 'New Mexico', 31: 'New York', 32: 'North Carolina', 33: 'North Dakota', 34: 'Ohio', 35: 'Oklahoma', 36: 'Oregon', 37: 'Pennsylvania', 38: 'Rhode Island', 39: 'South Carolina', 40: 'South Dakota', 41: 'Tennessee', 42: 'Texas', 43: 'Utah', 44: 'Vermont', 45: 'Virginia', 46: 'Washington', 47: 'West Virginia', 48: 'Wisconsin', 49: 'Wyoming'},
#  'x': {0: 139, 1: -204, 2: -203, 3: 57, 4: -297, 5: -112, 6: 297, 7: 275, 8: 220, 9: 182, 10: -317, 11: -216, 12: 95, 13: 133, 14: 38, 15: -17, 16: 149, 17: 59, 18: 319, 19: 288, 20: 312, 21: 148, 22: 23, 23: 94, 24: 49, 25: -141, 26: -61, 27: -257, 28: 302, 29: 282, 30: -128, 31: 236, 32: 239, 33: -44, 34: 176, 35: -8, 36: -278, 37: 238, 38: 318, 39: 218, 40: -44, 41: 131, 42: -38, 43: -189, 44: 282, 45: 234, 46: -257, 47: 200, 48: 83, 49: -134},
#  'y': {0: -77, 1: -170, 2: -40, 3: -53, 4: 13, 5: 20, 6: 96, 7: 42, 8: -145, 9: -75, 10: -143, 11: 122, 12: 37, 13: 39, 14: 65, 15: 5, 16: 1, 17: -114, 18: 164, 19: 27, 20: 112, 21: 101, 22: 135, 23: -78, 24: 6, 25: 150, 26: 66, 27: 56, 28: 127, 29: 65, 30: -43, 31: 104, 32: -22, 33: 158, 34: 52, 35: -41, 36: 138, 37: 72, 38: 94, 39: -51, 40: 109, 41: -34, 42: -106, 43: 34, 44: 154, 45: 12, 46: 193, 47: 20, 48: 113, 49: 90}}