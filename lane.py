from random import random
from car import Car
import random

class Lane():
    def __init__(self,position):
        self.cars=[Car((random.choice([300,400,500,270,290]),position[1])) for _ in range(3)]
        
        
    def get_cars_positions(self):
        return [x.pos() for x in self.cars]
        
    def move_cars(self):
        for x in self.cars:
            x.move()
        