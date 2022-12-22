import random
import turtle as t

# Import colorgram and grab colors from a hirst painting image, then run through the list of colors and create a tuple
# for each color and put them in the color list - only needed once to pull colors
# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)
#
# print(color_list)


color_list = [(26, 109, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (222, 137, 176),
              (143, 109, 57), (101, 197, 219), (206, 166, 29), (21, 58, 132), (212, 75, 91), (238, 89, 49),
              (141, 208, 227), (119, 192, 141), (6, 160, 87), (4, 186, 179), (106, 108, 198), (136, 29, 72),
              (98, 51, 37), (25, 153, 211), (228, 168, 188), (153, 213, 195), (173, 186, 221), (234, 174, 162),
              (30, 91, 95), (87, 47, 34), (34, 46, 84)]

tom = t.Turtle()
tom.pensize(20)
t.colormode(255)


def move_turtle():

    for _ in range(10):
        tom.pencolor(random.choice(color_list))
        tom.pendown()
        tom.forward(0)
        tom.penup()
        tom.forward(50)
    tom.penup()
    tom.left(90)
    tom.forward(50)
    tom.left(90)
    tom.forward(500)
    tom.right(180)

for _ in range(10):
    move_turtle()

t.exitonclick()
