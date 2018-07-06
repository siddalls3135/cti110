import turtle

t = turtle

t.shape()
t.speed(10)


t.width(3)
t.bgcolor('black')
t.begin_fill()
t.pencolor('silver')
t.fillcolor('teal')
for a in range(8):
    for b in range(8):
        t.forward(125)
        t.left(45)
    t.left(45)
t.end_fill()
t.hideturtle()
        


