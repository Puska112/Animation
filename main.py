import turtle as tu
from random import *


win = tu.Screen()
border = tu.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('red')
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)


ball = tu.Turtle()
ball.hideturtle()
ball.shape("circle")
ball.up()
randx = randint(-290, 290)
randy = randint(-290, 290)
ball.goto(randx, randy)
ball.showturtle()
speed_x = 3
speed_y = 4

while True:
    x, y = ball.position()
    if x + speed_x >= 300 or x + speed_x <= -300:
        speed_x = -speed_x
    if y + speed_y >= 300 or y + speed_y <= -300:
        speed_y = -speed_y
    ball.goto(x+speed_x, y+speed_y)


win.mainloop()