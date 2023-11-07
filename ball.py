from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid =1, stretch_len=1)
        self.goto(0,0)
        self.x_unit = 10
        self.y_unit = 10


    def move(self):
        self.penup()
        self.new_x = self.xcor() + self.x_unit
        self.new_y = self.ycor() + self.y_unit
        self.goto(self.new_x, self.new_y)

    def reverse_move(self):
        self.x_unit = self.x_unit * -1


    def detect_collide_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_unit = self.y_unit * -1

    def detect_collide_paddle(self):
        self.x_unit = self.x_unit * -1





