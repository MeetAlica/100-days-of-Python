# import colorgram
import turtle
import random

# colors = colorgram.extract('colors.jpg', 12)
# rgb_colors = []
# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   rgb_colors.append((r, g, b))

# print(rgb_colors)
color_list = [(205, 161, 87), (58, 88, 129), (144, 92, 42), (220, 207, 111), (135, 174, 198), (137, 27, 49), (154, 49, 84), (47, 56, 103)]
number_of_dots = 100

turtle.colormode(255)
brush = turtle.Turtle()
brush.hideturtle()
brush.speed("fastest")
brush.penup()

brush.setheading(225)
brush.forward(300)
brush.setheading(0)

for dot_count in range(1, number_of_dots + 1):
  brush.dot(30, random.choice(color_list))
  brush.forward(50)

  if dot_count % 10 == 0:
    brush.left(90)
    brush.forward(50)
    brush.left(90)
    brush.forward(500)
    brush.left(180)

turtle.Screen().exitonclick()
