from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.write(f"Level : {self.level}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level : {self.level}", align=ALIGNMENT, font=FONT)
