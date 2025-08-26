from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()


def draw_pic(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(60)
        draw_pic(myTurtle, lineLen - 3)


if __name__ == '__main__':
    draw_pic(myTurtle, 120)
