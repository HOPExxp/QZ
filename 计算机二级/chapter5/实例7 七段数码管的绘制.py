# import datetime, turtle
#
#
# # 绘制单段数码管
# def drawline(draw):
#     turtle.down() if draw else turtle.up()
#     turtle.fd(40)
#     turtle.right(90)
#
#
# def drawDigit(d):
#     drawline(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 2, 6, 8] else drawline(False)
#     turtle.left(90)
#     drawline(True) if d in [0, 4, 5, 6, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
#     drawline(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
#     # 跳转画笔到下一位置
#     turtle.left(180)
#     turtle.up()
#     turtle.fd(20)
#
#
# def drawDate(date):
#     for i in date:
#         drawDigit(eval(i))
#
#
# if __name__ == '__main__':
#     turtle.setup(800, 400, 200, 200)
#     turtle.up()
#     turtle.fd(-300)
#     turtle.pensize(5)
#     turtle.pencolor('black')
#     drawDate(datetime.datetime.now().strftime('%Y%m%d'))
#     turtle.done()
#     # 隐藏移动光标
#     turtle.hideturtle()

#改进版
import datetime,turtle

def gap():
    turtle.up()
    turtle.fd(5)
def drawline(data):
    gap()
    turtle.down() if data else turtle.up()
    turtle.fd(40)
    gap()
    #**
    turtle.right(90)
def drawDigit(d):
    drawline(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if d in [0, 2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if d in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    # 跳转画笔到下一位置
    turtle.left(180)
    turtle.up()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年',font = ('Arial',20,'normal'))
            turtle.pencolor('purple')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font = ('Arial',20,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '_':
            turtle.write('日',font = ('Arial',20,'normal'))
            turtle.fd(40)
        else:
            drawDigit(eval(i))
if __name__ == '__main__':
    turtle.setup(820, 400, 200, 200)
    turtle.up()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d_'))
    turtle.done()
    # 隐藏移动光标
    turtle.hideturtle()