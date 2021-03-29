import turtle
import random

turtle.shape("turtle")
turtle.speed(0)

for i in range(50):
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)

  turtle.color(red, green, blue)

  turtle.penup()
  turtle.forward(10)
  turtle.pendown()

  x = random.randint(-300, 300)
  y = random.randint(-300, 300)

  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()

  #Draw a rectangle
  #length and height to be random, between 10-100
  #fill in the color

  recLength = random.randint(10, 100)
  recHeight = random.randint(10, 100)

  turtle.begin_fill()
  turtle.forward(recLength)
  turtle.left(90)
  turtle.forward(recHeight)
  turtle.left(90)
  turtle.forward(recLength)
  turtle.left(90)
  turtle.forward(recHeight)
  turtle.end_fill()
  turtle.penup()

  x = random.randint(-300, 300)
  y = random.randint(-300, 300)

  turtle.goto(x, y)
  turtle.pendown()

  cirRadius = random.randint(10, 70)
  turtle.begin_fill()
  turtle.circle(cirRadius)
  turtle.end_fill()