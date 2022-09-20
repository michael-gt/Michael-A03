import turtle

def square(turt, length):
    for turns in range(4):
        turt.forward(length)
        turt.left(90)


def eq_triangle(turt, length):
    turt.begin_fill()
    turt.fillcolor("#8B0000")
    for turns in range(3):
        turt.forward(length)
        turt.left(120)
    turt.end_fill()



def wall(turt, width, height):
    turt.begin_fill()
    for corners in range(2):
        turt.forward(width)
        turt.left(90)
        turt.forward(height)
        turt.left(90)
    turt.end_fill()

    brick_width = width / 40
    brick_width = int(brick_width)

    brick_height = height / 20
    brick_height = int(brick_height)

    for num in range(brick_height):
        turt.left(90)
        turt.forward(10)
        for number in range(brick_width):
            turt.right(90)
            turt.forward(20)
            turt.right(90)
            turt.forward(10)
            turt.left(90)
            turt.forward(20)
            turt.left(90)
            turt.forward(10)
        turt.left(90)
        turt.forward(width)
        turt.left(180)
        turt.forward(10)
        turt.left(90)
        turt.forward(10)
        brick_width = brick_width - 1
        for bricks in range(brick_width):
            turt.right(90)
            turt.forward(20)
            turt.right(90)
            turt.forward(10)
            turt.left(90)
            turt.forward(20)
            turt.left(90)
            turt.forward(10)
        turt.right(90)
        turt.forward(20)
        turt.right(90)
        turt.forward(10)
        turt.left(90)
        turt.forward(10)
        turt.left(90)
        turt.forward(10)
        turt.left(90)
        turt.forward(width)
        turt.left(180)
        brick_width = brick_width + 1
    turt.right(90)
    turt.forward(height)
    turt.left(90)






def gate(turt):
    turt.begin_fill()
    turt.fillcolor("#654321")
    turt.forward(80)
    turt.left(90)
    turt.forward(80)
    for circle in range(20):
        turt.forward(6.3)
        turt.left(9)
    turt.forward(85)
    turt.end_fill()


def _Main_():
    wn = turtle.Screen()
    wn.bgcolor("green")
    grey = turtle.Turtle()
    grey.speed("fastest")
    grey.color("black")
    grey.penup()
    grey.backward(200)
    grey.right(90)
    grey.forward(200)
    grey.left(90)
    grey.fillcolor("grey")
    grey.pendown()
    wall(grey, 400, 200)
    grey.forward(400)
    wall(grey, 120, 300)
    grey.right(180)
    grey.forward(520)
    grey.right(180)
    wall(grey, 120, 300)
    grey.left(90)
    grey.forward(300)
    grey.penup()
    grey.left(90)
    grey.forward(20)
    grey.left(180)
    grey.pendown()
    eq_triangle(grey, 160)
    grey.penup()
    grey.forward(520)
    grey.pendown()
    eq_triangle(grey, 160)
    grey.penup()
    grey.forward(20)
    grey.right(90)
    grey.forward(300)
    grey.right(90)
    grey.forward(240)
    grey.right(180)
    grey.pendown()
    gate(grey)
    grey.hideturtle()
    wn.exitonclick()


_Main_()
