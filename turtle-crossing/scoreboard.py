from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align='Left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"         GAME OVER! \n Press ENTER to play again.", align='Center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

