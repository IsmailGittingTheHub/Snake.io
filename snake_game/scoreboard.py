from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.score_board()
        self.hideturtle()

    def score_board(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_board()


    # def game_over(self):
    #     self.goto(0, 0 )
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.score_board()

