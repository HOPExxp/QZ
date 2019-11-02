#抄制版
import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

# if __name__ == '__main__':
#     turtle.setup(800,400)
#     turtle.speed(5)
#     turtle.up()
#     turtle.goto(300,50)
#     turtle.down()
#     turtle.pensize(2)
#     koch(600,3)
#     turtle.hideturtle()
#     turtle.done()

#进阶版
if __name__ == '__main__':
    turtle.setup(800,800)
    turtle.speed(0)
    turtle.up()
    turtle.goto(-300,200)
    turtle.down()
    turtle.pensize(2)

    level = 5
    koch(600,level)
    turtle.right(120)
    koch(600,level)
    turtle.right(120)
    koch(600,level)

    turtle.hideturtle()
    turtle.done()