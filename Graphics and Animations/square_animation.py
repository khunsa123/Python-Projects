# -*- coding: utf-8 -*-
"""square-animation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C14sdzRCVh9OLySmwypAPAi0uPcjmnhP

There are 3 versiona of this animation. I used square shape in this program.

**Version 1:** Simple Animation by drawing squares in a circular motion.
"""

import turtle
turtle.bgcolor("gold")

squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("purple")

for i in range(400):
   squary.forward(i)
   squary.left(91)

"""**Version 2:** In this version after finishing the first shape it will start drwaing new shape from the last square of first shape. we can fill the full display area by using this logic."""

import turtle
turtle.bgcolor("crimson")

squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("aqua")

# Loop for drawing the square-like shape
for i in range(400):
    squary.forward(i)
    squary.left(91)

# Reverse the drawing by decreasing the value of i
for i in range(399, 0, -1):
    squary.forward(i)
    squary.left(91)

# Close the turtle graphics window when done
turtle.done()

"""**Version 3:** In this version we have reversed the out put of Version 1 after finishing the drawing. We have used undo() function to decrease the squares untill the go back to initial point."""

import turtle
turtle.bgcolor("black")

squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("red")

# Store the number of steps taken to draw the square
steps = []

# Loop for drawing the square-like shape
for i in range(400):
    squary.forward(i)
    squary.left(91)
    steps.append(i)

# Reverse the drawing by erasing the squares
for step in steps[::-1]:
    for _ in range(step):
        squary.undo()  # Erase a step

# Close the turtle graphics window when done
turtle.done()