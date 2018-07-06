import turtle

siddall = turtle

siddall.shape('turtle')

siddall.penup()
siddall.backward(100)
siddall.pendown()

i = 0

while i<4:
    siddall.forward(100)
    siddall.right(90)
    i = i+1

siddall.penup()
siddall.forward(150)
siddall.pendown()

i = 0

while i<3:
    siddall.forward(100)
    siddall.right(120)
    i = i+1
