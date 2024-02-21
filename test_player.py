STARTING_POSITION = (0,0)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
from math import atan,pi
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=6,stretch_len=1)

        self.speed("fastest")
        self.goto(0,0)
        self.setheading(90)
    def move(self,x,y):
        self.goto(self.xcor()+((517-x)/52),self.ycor()+((y-517)/52))
    def set_direction(self,x,y):
        if(x==0):
            c=90
        else:
            a=float(y/x)
            c=(atan(a)*180/pi)-45
        self.setheading(c)
    def finish(self):
        if self.ycor()==FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True