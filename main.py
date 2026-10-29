import turtle,colorsys

screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(800,800)
turtle.tracer(5,0)

t=turtle.Turtle()
t.speed(0)
t.hideturtle()

h=0

for i in range(200):
    r,g,b=colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(r,g,b)
    t.width(1)

    for _ in range(4):
     t.forward(i*1.2)
     t.left(90)

    t.left(5)
    h=(h+0.005)%1
turtle.update()    
turtle.done()