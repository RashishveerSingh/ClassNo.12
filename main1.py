# draw polygon
import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

namber_of_side = 6
len_side = 70
angle = 360 / namber_of_side
for i  in range(namber_of_side):
    polygon.forward(len_side)
    polygon.right(angle)
turtle.done()