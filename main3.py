import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(300,400)
turtle.Screen().title("spiral Pattern")
spiral = turtle.Turtle()
size = 0
count = 0
while count <= 10:
    for i in range(4):
        spiral.fd(size + 1)
        spiral.lt(90)
        size = size - 5
    count = count + 1
    size = size + 1
turtle.done()