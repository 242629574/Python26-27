from myFunctions import *

# Neon RGB Palette (Cyan, Magenta, Yellow, Purple)
cyber_colors = [
    (0, 255, 255),    #  Cyan
    (255, 0, 255),    #  Magenta
    (255, 255, 0),    #  Yellow
    (180, 0, 255),    #  Purple
]

bob.screen.colormode(255)
bob.screen.bgcolor("black")
bob.speed(0)
bob.hideturtle()


# Layer 1: Outer flower
bob.width(2)
for color in cyber_colors * 18:
    bob.pencolor(color)
    draw_petal()
    bob.right(5)

# Layer 2: Inner core
bob.width(2)
for color in cyber_colors * 9:
    bob.pencolor(color)
    draw_crystal()
    bob.right(10)

# Layer 3: Double ring border
draw_rings()

# Layer 4: Fill the corners neon stars
star_spots = [
    (-280, 190),
    (280, 190),
    (-280, -190),
    (280, -190),
    (-330, 0),
    (330, 0),
    (-210, 230),
    (210, -230),
    (-210, -230),
    (210, 230),
]

bob.width(2)
for x, y in star_spots:
    draw_star(x, y, cyber_colors)

turtle.done()

