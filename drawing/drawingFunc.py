from turtle import *
import random
def square(size):
    for i in range(3):
        forward(size)
        right(90)
    forward(size)
def bricks(amount, size):
    for x in range(amount):
        square(size)
        right(90)
        forward(size)
def multiSquare(amount, size):
    for x in range(amount):
        square(size)
        up()
        right(90)
        forward(size + 50)
        down()

def shapes(sides, size):
    for x in range(sides):
        forward(size)
        right(angle(sides))

def goodBye():
    bye()

def angle(sides):
    angle = 360 / sides
    return angle

def repeatShapes(sides, size, times):
    for x in range(times):
        up()
        forward(size)
        down()
        shapes(sides, size)
def reversal(sides, size):
        forward(size)
        right(180)
        shapes(sides, size)
def pat(sides, size, times):
    for x in range(times):
        repeat(sides, size, times)
        reversal(sides, size)
        repeat(sides, size, times - 1)
        right(90)
        up()
        forward(size)
        right(90)
        down()
def rev():
    right(180)

def usrColor():
    usrColor = raw_input("What color do you want to use? ")
    return usrColor

def usrFill():
    usrFill = raw_input("What background color do you want to put in? ")
    return usrFill

def setup():
    usrColor = raw_input("What color do you want to use? ")
    usrFill = raw_input("What fill do you want to put in? ")
    color = usrColor
    fill = usrFill
    speed = 10
def randomShape():
    ranSh = random.randint(3, 12)
    ranSi = random.randint(10, 40)
    shapes(ranSh, ranSi)

def star(size):
    for x in range(5):
        right(144)
        forward(size)

def randomStar():
    ranSi = random.randint(10, 70)
    ranAm = random.randint(10, 40)
    for x in range(ranAm):
        star(ranSi)
        randX = random.randint(-300, 300)
        randY = random.randint(-300, 300)
        up()
        goto(randX, randY)
        down()
color(usrColor())
bgcolor(usrFill())