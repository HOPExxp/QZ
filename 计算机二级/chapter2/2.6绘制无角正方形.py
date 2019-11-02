import turtle

def tiao():
    turtle.up()
    turtle.fd(20)
    turtle.down()

for i in range(4):
    tiao()
    turtle.fd(80)
    tiao()
    turtle.left(90)

