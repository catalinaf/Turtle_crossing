from turtle import Turtle
HEADING = 90
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.setheading(HEADING)
        self.go_to_start()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def start_new_level(self):
        if self.ycor() == FINISH_LINE_Y:
            self.go_to_start()
            return True
        else:
            return False
