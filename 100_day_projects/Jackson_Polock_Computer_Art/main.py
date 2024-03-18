import turtle
import time
import random
t = turtle.Turtle()
canvas = turtle.getscreen()

turtle.colormode(255)
num = random.randrange(1, 150)
canvas = turtle.bgcolor("gray")
t.pensize(15)
t.speed(10)

def forward():
    t.forward(num)
    for _ in range(4):
        t.forward(100)
        t.left(120)
        t.forward(100)

def backward():
    t.backward(num)
    for _ in range(5):
        t.forward(100) 
        t.left(90) 
 
def right():
    t.right(num)
    for _ in range(6):
        t.forward(90)
        t.left(300)

def left():
    t.left(num)

def circle():
    t.circle(num)

def color():
    r_color = random.randint(1, 255)
    g_color = random.randint(1, 255)
    b_color = random.randint(1, 255)
    t.color(r_color, g_color, b_color)

movements = [forward, backward, right, left, circle, color]

for _ in range(1, 101):
    random.choice(movements)()

# canvas = time.sleep(2)
canvas = turtle.Screen().exitonclick()
print()
print("The drawing is finished.")
print()
# canvas = turtle.done()