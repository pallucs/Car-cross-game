from turtle import Turtle

FORWARD = 20
BACKWARD = 20

class Hero(Turtle):
    def __init__(self):
        super().__init__()
        self.create_hero()
    
    def create_hero(self):
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(0,-230)
        self.setheading(90)
        self.pos_x_move = 10
        self.neg_x_move = -10
        
    def up(self):
        self.forward(FORWARD)
        
    def down(self):
        self.backward(BACKWARD)
        
    def right(self):
        new_x = self.pos_x_move + self.xcor()
        self.goto(new_x, self.ycor())
        
    def left(self):
        new_x = self.xcor() + self.neg_x_move
        self.goto(new_x, self.ycor())
        
    def reset(self):
        self.goto((0,-230))