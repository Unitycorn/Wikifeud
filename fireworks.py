import turtle
import random

colors = ["red", "yellow", "green", "cyan", "orange", "purple", "pink",
              "magenta", "blue", "turquoise", "gold", "violet", "lime"]

def single_firework(x,y, size):
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(50)
    t.hideturtle()

    t.penup()
    t.goto(x, y)
    t.pendown()

    for i in range(36):
        #jede einzelne Feuerwerksexplosion
        t.color(random.choice(colors))
        t.forward(size)
        t.backward(size)
        t.right(10)

def full_fireworks():
    for repetition in range(5):
        x = random.randint(-100, 200)
        y = random.randint(-100, 200)
        size = random.randint(50, 100)
        single_firework(x, y, size)


if __name__ == "__main__":
    pass