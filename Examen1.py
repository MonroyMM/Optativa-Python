import turtle
import random

def circulos(turtle):
  rad=[10,11,12,13,14,15,16,17,18,19,20]
  random_rad=random.choice(rad)

  turtle.circle(random_rad)

  posx=random.randint(-100,100)
  posy=random.randint(-100,100)

  turtle.penup()
  turtle.goto(posx,posy)
  turtle.pendown()

  colores = ['red', 'blue', 'green', 'black']
  random_color = random.choice(colores)
  turtle.pencolor(random_color)

 
screen = turtle.Screen()
screen.setup(width=800, height=600)

grafico=turtle.Turtle()

for i in range(20):
 circulos(grafico)