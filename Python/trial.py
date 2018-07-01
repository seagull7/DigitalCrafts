from turtle import *
from shapes import *
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
forward(random.randint(1,200))
right(random.randint(1, 360))
craytriangle()
forward(random.randint(1,200))
right(random.randint(1, 360))
craystar()
forward(random.randint(1,200))
right(random.randint(1, 360))
craytriangle()
forward(random.randint(1,200))
right(random.randint(1, 360))
craystar()
forward(random.randint(1,200))
right(random.randint(1, 360))
craytriangle()
mainloop()

        
