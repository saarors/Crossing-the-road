from turtle import Screen, Turtle
from .objects import Player, Road, Car, Scoreboard
from time import sleep, time
from random import randint


DEFAULT_GAMESIZE = {"width": 1250, "height": 800}
SPAWN_INTERVAL = 0

class Game:
    def __init__(self):
        screen = Screen()
        screen.tracer(0)
        screen.title("Turtle Game")
        screen.bgcolor("lightgreen")
        screen.setup(**DEFAULT_GAMESIZE)
        self.player = None
        self.game_on = True
        self.last_spawn = time()
        self.spawn_interval = 0
        self.screen = screen
        self.level = 1
        self.scoreboard = Scoreboard(self.level)
        self.cars = []
        self.play()

    def spawn_cars(self):
        LEVEL_MULTIPLIERS = {
            1: {"speed": 3, "quantity": 40},
            2: {"speed": 4, "quantity": 60},
            3: {"speed": 7, "quantity": 80},
            4: {"speed": 10, "quantity": 80},
            5: {"speed": 12, "quantity": 100}
        }
        speed = LEVEL_MULTIPLIERS.get(self.level).get("speed")
        quantity = LEVEL_MULTIPLIERS.get(self.level).get("quantity")

        if len(self.cars) < quantity and time() - self.last_spawn > self.spawn_interval:
            starting_position = (-1000, randint(-250, 250))
            car = Car(speed, starting_position)
            self.cars.append(car)
            self.last_spawn = time()
        self.screen.update()
        self.spawn_interval = 0.2

    def move_cars(self):
        for _car in self.cars:
            if _car.xcor() > 1000:
                self.cars.remove(_car)
            else:
                _car.move()

            if self.player.distance(_car) < 25:
                self.win = False
                self.game_on = False

    def check_player(self):
        if self.player.ycor() > 310:
            self.level += 1
            self.scoreboard.add_level()
            if self.level == 6:
                self.win = True
                self.game_on = False
            self.player.setpos(0, -400)


    def listen(self):
        self.screen.listen()
        self.screen.onkeypress(self.player.move_up,"w")
        self.screen.onkeypress(self.player.move_down, "s")
        self.screen.onkeypress(self.player.move_left, "a")
        self.screen.onkeypress(self.player.move_right, "d")

    def play(self):
        # Generate Objects
        road = Road()
        self.player = Player()
        self.player.setheading(90)

        while self.game_on:
            self.listen()
            self.screen.update()
            self.spawn_cars()
            self.move_cars()
            self.check_player()
            sleep(0.001)

        self.player.clear()
        self.scoreboard.clear()
        sign = Turtle()
        sign.penup()
        sign.hideturtle()
        sign.setpos(0, 350)
        sign.pencolor("black")
        if self.win:
            sign.write("YOU WIN!", align="center", font=("Courier", 30, "bold"))
        else:
            sign.write("YOU LOSE!", align="center", font=("Courier", 30, "bold"))
        self.screen.update()
        self.screen.exitonclick()






