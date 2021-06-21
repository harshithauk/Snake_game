from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.normal_food()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)

    def food_fest(self):
        self.shapesize(1, 1)
        self.color("red")

    def normal_food(self):
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("white")
