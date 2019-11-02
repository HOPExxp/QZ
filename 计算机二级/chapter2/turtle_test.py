import turtle
# turtle.fd(20)

# turtle.circle(90,360)
for i in range(-1,-10,-1):
    turtle.circle(-10*i,360)
    turtle.seth(-90)
    turtle.up()
    turtle.fd(10)
    turtle.down()
    turtle.seth(0)
turtle.done()


