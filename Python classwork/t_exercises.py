from turtle import *
from shapes import *
#1-
    #1.triangle
def eTriangle():
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
    right(120)
    mainloop()
    #2.square
def square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    mainloop()
    #3.pentagon
def pentagon():
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    mainloop()
    #4.hexagon
def hexagon():
    forward(100)
    right(60)
    forward(100)
    right(60)
    forward(100)
    right(60)
    forward(100)
    right(60)
    forward(100)
    right(60)
    forward(100)
    mainloop()
    #5.octagon
def octagon():
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    mainloop()
    #6.star
def star():
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)
    mainloop()
    #7.circle
def circle():
    for i in range(370):
        forward(2)
        right(1)
    mainloop()

#2- 
from shapes import *
eTriangle()
square()
pentagon()
hexagon()
octagon()
star()
circle()
mainloop()

#3- 
bgcolor("MidnightBlue")
starp(20, True, "yellow", "MidnightBlue")
right (20)
forward(100)

starp(20, True, "yellow", "MidnightBlue")
right (30)
forward(150)

starp(20, True, "yellow", "MidnightBlue")
right (40)
forward(200)

starp(20, True, "yellow", "MidnightBlue")
right (50)
forward(250)

starp(20, True, "yellow", "MidnightBlue")
right (60)
forward(300)

starp(20, True, "yellow", "MidnightBlue")

forward(100)

starp(20, True, "yellow", "MidnightBlue")

forward(100)

starp(20, True, "yellow", "MidnightBlue")

left (90)
forward(300)

starp(20, True, "yellow", "MidnightBlue")
right (50)
forward (300)

starp(20, True, "yellow", "MidnightBlue")
right(50)
forward(300)

starp(20, True, "yellow", "MidnightBlue")

right (50)

forward (275)

circlep(3, True, "SlateGrey", "MidnightBlue")
right(60)
forward(20)



mainloop()


#4- 
bgcolor("skyblue")
right(90)
penup()
forward(100)
right(90)
forward(200)

fillcolor("Green")
begin_fill()
forward (300)
left(90)
forward (300)
left(90)
forward(1250)
left(90)
forward(300)
left(90)
forward(1000)
end_fill()

right (90)

pendown()
rectangle(200, 450, True, "Red")
left(180)
forward(200)
left(90)
penup()
forward(100)
right(90)
pendown
rectangle(50, 100, True, "Brown")

penup()
right(90)
forward(50)
right(90)
forward(50)
right (90)
forward(10)

circle(.1, True, "Black")

penup()
forward(40)
left(90)
forward(50)

pendown()
fillcolor("grey")
begin_fill()
left (20)
forward(400)
left (75)
forward(50)
left(105)
forward(400)
left(75)
forward(50)
end_fill()

right(5)
penup()
forward(200)
right(90)
forward(200)
right(90)
left(40)
pendown()
fillcolor("brown")
begin_fill()
forward(293.717)
right(80)
forward(293.717)
right(140)
forward(450)
end_fill()

penup()
left(90)
forward(75)
left(90)
forward(75)
pendown()
square(50, True, "blue", "Black")
right(90)
square(25, False, "blue", "black")
right(90)
forward(50)
right(90)
forward(25)
square(25, False, "blue", "black")

penup()
left(90)
forward(25)
right(90)
forward(200)
pendown()
square(50, True, "blue", "Black")
right(90)
square(25, False, "blue", "black")
right(90)
forward(50)
right(90)
forward(25)
square(25, False, "blue", "black")

penup()
left(90)
forward(250)
left (90)
forward(400)

circlep(3, True, "yellow", "yellow")
mainloop()

#5- 

def door():
    rectangle(50, 100, True, "Brown")
    penup()
    right(90)
    forward(50)
    right(90)
    forward(50)
    right (90)
    forward(10)

    circle(.1, True, "Black")


def grass():
    fillcolor("Green")
    begin_fill()
    forward (300)
    left(90)
    forward (300)
    left(90)
    forward(1250)
    left(90)
    forward(300)
    left(90)
    forward(1000)
    end_fill()

def house():
    rectangle(200, 450, True, "Red")
    

def roof():
    fillcolor("brown")
    begin_fill()
    forward(293.717)
    right(80)
    forward(293.717)
    right(140)
    forward(450)
    end_fill()

def window():
    square(50, True, "blue", "Black")
    right(90)
    square(25, False, "blue", "black")
    right(90)
    forward(50)
    right(90)
    forward(25)
    square(25, False, "blue", "black")

def sun():
    circlep(3, True, "yellow", "yellow")

def sidewalk():
    fillcolor("grey")
    begin_fill()
    left (20)
    forward(400)
    left (75)
    forward(50)
    left(105)
    forward(400)
    left(75)
    forward(50)
    end_fill()








bgcolor("skyblue")
right(90)
penup()
forward(100)
right(90)
forward(200)

grass()

right (90)
pendown()

house()

left(180)
forward(200)
left(90)
penup()
forward(100)
right(90)
pendown

door()

penup()
forward(40)
left(90)
forward(50)
pendown()

sidewalk()

right(5)
penup()
forward(200)
right(90)
forward(200)
right(90)
left(40)
pendown()

roof()

penup()
left(90)
forward(75)
left(90)
forward(75)

pendown()

window()

penup()
left(90)
forward(25)
right(90)
forward(200)
pendown()

window()

penup()
left(90)
forward(250)
left (90)
forward(400)

sun()
mainloop()

#6- 
import random

def craystar():
    color('red', 'yellow')
    begin_fill()
    for i in range(36):
        forward(200)
        left(170)
    end_fill()  

def craytriangle():
    color('black', 'blue')
    begin_fill()
    i = 60
    
    while i > 0:
        forward(i)
        right(120)
        i -= 5
    end_fill()

def craysquare():
    color("green", "Blue")
    begin_fill()
    for i in range(12):
        for i in range(4):
            forward(60)
            right(90)
        for i in range(12):
            forward (random.randint(1,60))
            right(90)
    end_fill()


craysquare()
forward (50)
craysquare()
forward (50)
craysquare()
forward (50)
craystar()
forward(random.randint(1,100))
right(random.randint(1, 90))
craytriangle()
forward(random.randint(1,100))
right(random.randint(1, 90))
craystar()
forward(random.randint(1,100))
right(random.randint(1, 90))
craytriangle()
forward(random.randint(1,100))
right(random.randint(1, 90))
craystar()
forward(random.randint(1,100))
right(random.randint(1, 90))
craytriangle()
mainloop()