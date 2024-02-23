from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.positions = [(0.00, 0.00), (-10.00, 0.00), (-20.00, 0.00)]
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for position in self.positions:
            self.create_snake_a_body(position)

    def create_snake_a_body(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape("circle")
        snake.setposition(position)
        self.snake_list.append(snake)
        snake.color("white")

    def snake_extend(self):
        self.create_snake_a_body(self.snake_list[-1].position())

    def move(self):
        self.head.shape('turtle')
        for go_no in range(len(self.snake_list) - 1, 0, -1):
            new_positionX = self.snake_list[go_no - 1].xcor()
            new_positionY = self.snake_list[go_no - 1].ycor()
            self.snake_list[go_no].goto(new_positionX, new_positionY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for snake in self.snake_list:
            snake.goto(10000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]
