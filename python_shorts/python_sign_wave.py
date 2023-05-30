import turtle
import math

# Set up the turtle window
window = turtle.Screen()
window.setup(500, 700, 70, 200)
window.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("white")
pen.speed(0)

# Set the amplitude and frequency of 
# the sine wave
amplitude = 100
frequency = 10

# Calculate the wavelength based on the \
# frequency
wavelength = (
    window.window_width() // frequency) * 4
pen.goto(-300, 0)
pen.goto(350, 0)


# Main loop for drawing the sine wave
for x in range(-wavelength , wavelength + 50):
    # Calculate the corresponding 
    # y-coordinate based on the sine 
    # function
    y = amplitude * math.sin(
        2 * math.pi * x / (wavelength // 4))

    # Move the turtle to the calculated 
    # position
    pen.goto(x, y)


# Keep the turtle window open
turtle.mainloop()





