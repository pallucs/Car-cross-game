from turtle import Turtle, position

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write('Score : {}'.format(self.score), align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.clear()
        self.write('Game Over', align=ALIGNMENT, font=FONT)