from turtle import Turtle
import random

colors = ['red','green','blue','yellow','orange']


class Car(Turtle):
    def __init__(self,position):
        super().__init__()
        self.position = position
        self.create_cars()
    def create_cars(self):
        self.shape('square')
        self.color(random.choice(colors))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(self.position)
        
    def move(self):
        self.setheading(180)
        self.forward(random.randint(2,10))
        if self.xcor()<-250:
            self.goto(self.position)