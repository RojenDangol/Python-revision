from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_left(self):
        self.left(90)
        self.forward(MOVE_DISTANCE)
        self.right(90)

    def go_right(self):
        self.right(90)
        self.forward(MOVE_DISTANCE)
        self.left(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        return self.ycor() > FINISH_LINE_Y


