from turtle import *

sc = Screen()
sc.setup(600, 600)
image = "snake.gif"
sc.addshape(image)
t = Turtle()
t.shape(image)
mainloop()
sc.listen()
sc.onkey(clear, "space")