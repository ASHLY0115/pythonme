import turtle

def draw_hexagon(x,y,color,side):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(6):
        t.forward(side)
        t.left(60)
    
    t.end_fill()
    t.up()
    t.home()
    t.down()

t=turtle.Turtle()
draw_hexagon(0,-100,"red",200)

t.hideturtle()
turtle.done()
