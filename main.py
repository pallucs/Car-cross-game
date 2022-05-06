from turtle import Screen
from hero import Hero
from scoreboard import Scoreboard
from lane import Lane

import time

WIDTH = 500
HEIGHT = 500

screen = Screen()

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('white')
screen.title('Turtle Cross')
screen.tracer(0)

hero = Hero()
scoreboard = Scoreboard((-150, 220))


screen.listen()

screen.onkey(hero.up, 'Up')
screen.onkey(hero.down, 'Down')

screen.onkey(hero.right, 'Right')
screen.onkey(hero.left, 'Left')

game_is_on = True

lan1 = Lane((230,0))
lan2 = Lane((230,60))
lan3 = Lane((230,120))
lan4 = Lane((230,-60))
lan5 = Lane((230,-120))

while game_is_on:
    time.sleep(0.1)
    screen.update()
    lan1.move_cars()
    lan2.move_cars()
    lan3.move_cars()
    lan4.move_cars()
    lan5.move_cars() 
    #DETECT COLLISION WITH CARS
    positions=lan1.get_cars_positions()+lan2.get_cars_positions()+lan3.get_cars_positions()+lan4.get_cars_positions()+lan5.get_cars_positions()
    for pos in positions:
        if hero.distance(pos) < 15:
            game_is_on = False
            scoreboard.game_over()
            
    #DETECT IF THE TURTLE CROSSED THE CARS
    if hero.ycor() > 230:
        scoreboard.increase_score()
        hero.reset()
        
screen.exitonclick()