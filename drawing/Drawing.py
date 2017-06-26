import turtle

turtle.setup()
turtle.screensize(400, 300)
turtle.title("Handling keypresses!")
turtle.bgcolor("lightblue")
squirt = turtle.Turtle()

def sraight():
    squirt.forward(20)

def angleRight():
    squirt.left(30)

def angleLeft():
    squirt.right(30)

def goodBye():
    turtle.bye()

def lift():
    up()

def unlift():
    down()

def startOver():
    turtle.clear()
    

turtle.onkey(sraight, "Up")
turtle.onkey(angleLeft, "Left")
turtle.onkey(angleRight, "Right")
turtle.onkey(lift, "p")
turtle.onkey(unlift, "o")
turtle.onkey(goodBye, "q")
turtle.onkey(startOver, "r")

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Aaron(turtle.Turtle):
#     def paint(self,x,y):
#         self.fillcolor("red")

#     def unpaint(self,x,y):
#         self.fillcolor(" ")

# squirt = Aaron()
# squirt.onclick(squirt.paint)
# squirt.onrelease(squirt.unpaint)
# squirt.ondrag(squirt.goto)


turtle.listen()
turtle.mainloop()
turtle.done()