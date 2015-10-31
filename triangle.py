import turtle

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    for i in range(1,37):
        draw_triangle(brad)
        brad.right(10)
    #create the turtle Angie - Draws a circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    window.exitonclick()

draw_art()
