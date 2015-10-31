import turtle


window = turtle.Screen()
window.bgcolor("red")
def draw_square():
    brad = turtle.Turtle()  # created an instance of class Turtle
    brad.shape("turtle")
    brad.speed(1)
    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")
    angie.circle(100)

draw_square()
draw_circle()
window.exitonclick()
