from turtle import *

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

def repeat(sides, size, times):
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

def setup():
    usrColor = raw_input("What color do you want to use? ")
    usrFill = raw_input("What fill do you want to put in? ")
    color = usrColor
    fill = usrFill
    speed = 10

onkey(goodBye, "q")
for x in range(3):
    pat(12, 40, 2)
    rev()
listen()
mainloop()
done()