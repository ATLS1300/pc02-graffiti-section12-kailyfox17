#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======




#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()

turtle.up()
turtle.goto(-25,185)
turtle.color("green")
turtle.down()
turtle.begin_fill()
turtle.pensize(8)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.right(180)
turtle.forward(50)
turtle.right(90)
turtle.right(180)
turtle.forward(200)
turtle.right(90)
turtle.right(180)
turtle.forward(50)
turtle.right(90)
turtle.right(180)
turtle.forward(100)
turtle.end_fill()
turtle.up()

turtle.color("light green")
turtle.right(90)
turtle.forward(49)
turtle.right(90)
turtle.down()
turtle.forward(50)
turtle.right(90)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.right(180)
turtle.forward(50)
turtle.up()

turtle.goto(25,10)
turtle.color("orange")
turtle.down()
turtle.forward(15)
turtle.right(90)
turtle.right(45)
turtle.forward(30)
turtle.begin_fill()
turtle.forward(30)
turtle.right(180)
turtle.forward(60)
turtle.right(180)
turtle.right(45)
turtle.right(45)
turtle.forward(60)
turtle.left(90)
turtle.left(45)
turtle.forward(40)

turtle.up()
turtle.goto(33,190)
turtle.color("black")
turtle.right(180)
turtle.right(45)
turtle.forward(20)
turtle.left(90)
turtle.forward(30)
turtle.begin_fill()
turtle.pensize(4)
turtle.down()
turtle.circle(10)
turtle.circle(20)
turtle.end_fill()












