# import colorgram
#
# def get_colours_list(image_name, colors_number):
#     """Extract colors_number colors from an image
#     Returns list of rgb colours"""
#     colors = colorgram.extract(image_name, colors_number)
#     colors_list = []
#     for color in colors:
#         colors_list.append(tuple(rgb for rgb in color.rgb))
#     return colors_list
#
#
# color_list = get_colours_list('image.jpg', 100)
# print(len(color_list))
# print(color_list)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(253, 253, 249), (251, 244, 248), (247, 252, 250), (236, 246, 250), (243, 234, 76), (211, 158, 93),
              (188, 12, 69), (111, 179, 208), (25, 116, 169), (172, 172, 31), (221, 128, 166), (160, 78, 35),
              (128, 186, 146), (10, 32, 76), (235, 73, 41), (217, 67, 108), (31, 135, 83), (176, 48, 95),
              (234, 165, 194), (79, 13, 63), (12, 55, 34), (236, 228, 6), (29, 164, 207), (15, 42, 132), (58, 165, 95),
              (135, 213, 228), (9, 102, 63), (134, 36, 21), (93, 29, 12), (156, 211, 190), (6, 93, 107), (253, 4, 67),
              (108, 88, 8), (78, 130, 189), (228, 175, 166), (184, 186, 208)]
tim.speed(0)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(500)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(60, random.choice(color_list))
    tim.forward(60)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(60)
        tim.setheading(180)
        tim.forward(600)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
