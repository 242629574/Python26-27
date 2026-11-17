
import turtle

bob = turtle.Turtle()

# 1. Helper to move without leaving a trail
def jump_to(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()


# 2. petals
def draw_petal():
    bob.circle(140, 60)
    bob.left(120)
    bob.circle(140, 60)
    bob.left(120)


# 3. diamond petlas
def draw_crystal():
    for _ in range(4):
        bob.forward(75)
        bob.left(60)
        bob.forward(75)
        bob.left(120)


# 4. Double ring frame
def draw_rings():
    jump_to(0, -175)
    bob.width(3)
    bob.pencolor((0, 255, 255))
    bob.circle(175)

    jump_to(0, -190)
    bob.width(2)
    bob.pencolor((255, 0, 255))
    bob.circle(190)


# 5. stars
def draw_star(x, y, colors):
    jump_to(x, y)

    for color in colors:
        bob.pencolor(color)
        bob.forward(28)
        bob.backward(28)
        bob.right(90)
