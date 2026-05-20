import turtle
from turtle import Turtle
from random import choice
from .common import get_randomcolor

DEATH_COLORS = [(255, 0, 0), (220, 20, 60), (178, 34, 34), (250, 128, 114)]
ROAD_COLOR = (176, 176, 176)
PLAYER_COLOR = (255, 255, 255)
PLAYER_STARTPOS = (0, -350)
PLAYER_SPEED = 20
ROAD_SIZE = {"stretch_wid": 30, "stretch_len": 100}

turtle.colormode(255)

class Scoreboard(Turtle):
    def __init__(self, level: int):
        super().__init__()
        self.level = level
        self.hideturtle()
        self.penup()
        self.setpos(-500, 350)
        self.color("black")
        self.display()

    def add_level(self):
        self.level += 1
        self.clear()
        self.display()

    def display(self):
        self.write(f"Level: {self.level}/5", align="center", font= ("Courier", 20, "bold"))



class Car(Turtle):
    def __init__(self,
                 speed: float,
                 starting_position: tuple[float, float]):
        super().__init__()

        self.color(get_randomcolor())
        self._speed = speed
        self.shape("square")
        self.shapesize(stretch_len=3.25, stretch_wid=2)
        self.penup()

        # Set Car
        self.setpos(starting_position)

    def move(self):
        self.forward(self._speed)

class Player(Turtle):
    def __init__(self,
                 speed: int = 30,
                 starting_position: tuple[float, float] = PLAYER_STARTPOS):
        super().__init__()
        self.color(PLAYER_COLOR)
        self.shape("turtle")
        self.penup()
        self._speed = speed
        self.setpos(starting_position)

    def move(self, x_chg: int = 0, y_chg: int = 0):
        self.goto(x=self.xcor() + x_chg, y=self.ycor() + y_chg)

    def move_up(self):
        self.move(y_chg=self._speed)

    def move_down(self):
        self.move(y_chg=-self._speed)

    def move_left(self):
        self.move(x_chg=-self._speed)

    def move_right(self):
        self.move(x_chg=self._speed)

    def die(self):
        for x in range(40):
            self.color(choice(DEATH_COLORS))
            self.setheading(self.heading() + x)

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.color(ROAD_COLOR)
        self.shape("square")
        self.shapesize(**ROAD_SIZE)
