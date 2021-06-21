from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.display_score()

    def read_highscore(self):
        with open("data.txt") as file2:
            return int(file2.read())

    def add_score(self, new_score):
        self.score += new_score
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f" Score : {self.score} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False,  ALIGNMENT, FONT)