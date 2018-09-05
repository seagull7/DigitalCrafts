from turtle import *

#1-
    #1.triangle
def eTriangle(size, fill, color):
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(120)
    for i in range(size):  
        forward(1)
    right(120)
    for i in range(size):  
        forward(1)
    right(120)
    if fill:
        end_fill()
  
    #2.square
def square(size, fill, color):
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(90)
    for i in range(size):  
        forward(1)
    right(90)
    for i in range(size):  
        forward(1)
    right(90)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()
    
    #3.pentagon
def pentagon(size, fill, color):
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(72)
    for i in range(size):  
        forward(1)
    right(72)
    for i in range(size):  
        forward(1)
    right(72)
    for i in range(size):  
        forward(1)
    right(72)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()

    #4.hexagon
def hexagon(size, fill, color):
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()
        
    #5.octagon
def octagon(size, fill, color):
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()
    
    #6.star
def star(size, fill, color):
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    right(108)
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    right(108)
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    right(108)
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    right(108)
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()
    
    #7.circle
def circle(size, fill, color):
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(360):
        forward(size)
        right(1)
    if fill:
        end_fill()

def rectangle(sizeL, sizeW, fill, color):
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(sizeL):  
        forward(1)
    right(90)
    for i in range(sizeW):  
        forward(1)
    right(90)
    for i in range(sizeL):  
        forward(1)
    right(90)
    for i in range(sizeW):  
        forward(1)
    if fill:
        end_fill()


 #####


 ####


 ##


 #

 #with pen color

def circlep(size, fill, color, color2):
    pencolor(color2)
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(360):
        forward(size)
        right(1)
    if fill:
        end_fill()

    #1.triangle
def eTrianglep(size, fill, color, color2):
    pencolor(color2)
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(120)
    for i in range(size):  
        forward(1)
    right(120)
    for i in range(size):  
        forward(1)
    right(120)
    if fill:
        end_fill()
  
    #2.square
def square(size, fill, color, color2):
    pencolor(color2)
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(90)
    for i in range(size):  
        forward(1)
    right(90)
    for i in range(size):  
        forward(1)
    right(90)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()
    
    #3.pentagon
def pentagon(size, fill, color, color2):
    pencolor(color2)
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(72)
    for i in range(size):  
        forward(1)
    right(72)
    for i in range(size):  
        forward(1)
    right(72)
    for i in range(size):  
        forward(1)
    right(72)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()

    #4.hexagon
def hexagonp(size, fill, color, color2):
    pencolor(color2)
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    right(60)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()
        
    #5.octagon
def octagonp(size, fill, color, color2):
    pencolor(color2)
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    right(45)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()
    
    #6.star
def starp(size, fill, color, color2):
    pencolor(color2)
    fillcolor(color)
    if fill:
        begin_fill()
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    right(108)
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    right(108)
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    right(108)
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    right(108)
    for i in range(size):  
        forward(1)
    left (36)
    for i in range(size):  
        forward(1)
    if fill:
        end_fill()

