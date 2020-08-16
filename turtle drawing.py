import turtle

def colorfuloctagon():
    t = turtle.Turtle()
    t.pensize(3)
    t.speed(100)
    colors = ["red","orange","green","blue"]
    for x in range(200):
        t.forward(2*x)
        t.color(colors[x % 4])
        t.left(45)

colorfuloctagon()

input('hit enter to exit')


