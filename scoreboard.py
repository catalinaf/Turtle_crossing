from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.up()
        self.hideturtle()
        self.level = 0
        self.setposition(-230, 270)
        self.update_score_board()

    def update_score_board(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, "center", FONT)
