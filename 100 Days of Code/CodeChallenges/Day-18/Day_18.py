import random
import turtle as t
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
# 10 x 10 spots,  20 size 50 paces space. filled dots
tom = t.Turtle()
tom.pensize(20)
t.colormode(255)
dot_count = 0

def move_turtle():
    tom.pendown()
    tom.forward(0)
    tom.penup()
    tom.forward(50)
    


while dot_count < 10:
    move_turtle()
    dot_count += 1

t.exitonclick()
