import turtle

'''
The Sierpinski Triangle drawn by a Turtle

Ruleset:
x -> y+x+y
y -> x-y-x

Start:
x
'''

# how to substitude
x_substitude = "y+x+y"
y_substitude = "x-y-x"

# initial setup
tape_a = "x"
tape_b = ""

# number of substitutions
n = 11

# create
for i in range(n):
    for read in tape_a:
        if read == "x":
            tape_b = tape_b + x_substitude
        elif read == "y":
            tape_b = tape_b + y_substitude
        else:
            tape_b = tape_b + read
    tape_a = tape_b
    tape_b = ""

# turtle setup
turtle.speed(0)
#turtle.tracer(800,800)  # Massive Turtle Speed Up
turtle.penup()
turtle.goto(-380, -380)
turtle.pendown()

# draw
for read in tape_a:
    if read in ["x","y"]:
        turtle.forward(3)
    elif read == "+":
        turtle.pen(fillcolor="red", pencolor="red")
        turtle.left(60)
    else:
        turtle.pen(fillcolor="blue", pencolor="blue")
        turtle.right(60)

input("Press any key to close ...")
