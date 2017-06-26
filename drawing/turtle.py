from turtle import *

def turtleSquare():
    size = int(size)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

def turtleBricks(amount, size):
    x = 0
    while x >= amount:
        turtleSquare(size)
        right(90)
        forward(size)
        x += 1

def turtleSquares(amount, size):   
    x = 0
    while x <= amount:
        up()
        right(90)
        forward(size + 50)
        down()
def turtleColorCircle(color, width):
    pencolor(color)
    width(width)
    circle(180)
def turtleStar():
    for i in range(5):
        forward(100)
        right(144)

def mainloop():
    turtleSquare()
    #turtleBricks(3, 100)
    #turtleSquares(3, 100)
    #turtleColorCircle(red, 100)
    #turtleStar()

mainloop()