import turtle

'''
The Sierpinski Triangle drawn by a Turtle

Ruleset:
x -> y+x+y
y -> x-y-x

Start:
x
'''

x_substitude = "y+x+y"
y_substitude = "x-y-x"


tape_a = "x"
tape_b = ""

n = 11

for i in range(0, n):
    for read in tape_a:
        if read == "x":
            tape_b = tape_b + x_substitude
        elif read == "y":
            tape_b = tape_b + y_substitude
        else:
            tape_b = tape_b + read
    tape_a = tape_b
    tape_b = ""

turtle.speed(0)
turtle.penup()
turtle.goto(-400, -400)
turtle.pendown()

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
