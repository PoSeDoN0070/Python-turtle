import turtle
import colorsys

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Spiral Drawing")

spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)
spiral.hideturtle()

# Draw a colorful spiral using HSV color space
num_colors = 360

for i in range(300):
    # Convert HSV color to RGB
    color = colorsys.hsv_to_rgb(i / num_colors, 1, 1)
    spiral.pencolor(color)

    spiral.forward(i * 0.5)
    spiral.right(59)  # Spiral angle choice

screen.mainloop()
