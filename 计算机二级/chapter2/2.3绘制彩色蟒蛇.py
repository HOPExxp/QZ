# #e2.3DrawPython.py   ---  源码
# import turtle
# def drawSnake(radius, angle, length):
#     turtle.seth(-40)
#     for i in range(length):
#         turtle.circle(radius, angle)
#         turtle.circle(-radius, angle)
#     turtle.circle(radius, angle/2)
#     turtle.fd(40)
#     turtle.circle(16, 180)
#     turtle.fd(40* 2/3)
# turtle.setup(650, 350, 200, 200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor("purple")
# drawSnake(40, 80, 4)
# turtle.done()

#彩色蛇
import turtle
import random
def drawSnake(radius, angle, length,color):
    turtle.seth(-40)
    for i in range(length):
        chioce = random.randint(0,9)
        turtle.pencolor(color[chioce])
        turtle.circle(radius, angle)
        turtle.circle(-radius, angle)
    chioce = random.randint(0, 9)
    turtle.pencolor(color[chioce])
    turtle.circle(radius, angle/2)
    turtle.fd(40)
    chioce = random.randint(0, 9)
    turtle.pencolor(color[chioce])
    turtle.circle(16, 180)
    turtle.fd(40* 2/3)
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
# turtle.pencolor("purple")
color = ['green','black','grey','darkgreen','gold','violet','purple','yellow','red','blue']
drawSnake(40, 80, 4,color)
turtle.done()
