
import turtle

t = turtle

t.width(20)

t.color('orange')

t.shape("turtle")

t.pencolor('silver')

t.penup()

t.backward(200), t.pendown(), t.backward(100), t.right(90)
t.forward(100), t.left(90), t.forward(100), t.right(90)
t.forward(100), t.right(90), t.forward(100), t.right(180)
t.penup(), t.forward(200), t.pendown(), t.forward(100), t.left(90)
t.forward(100), t.left(90), t.forward(100), t.right(90)
t.forward(100), t.right(90), t.forward(100), t.penup()
t.forward(50),t.pendown()

t.exitonclick()


