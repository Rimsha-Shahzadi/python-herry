# first game
import pygame as py
from pygame.locals import MOUSEBUTTONUP
size = (500, 400)
screen = py.display.set_mode(size)
while True:
    for ev in py.event.get():
        if ev.type == MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            col = (0, 225, 255)
            py.draw.circle(            
            screen, col, pos, 20, 5
            )
            py.display.update()
# second game

import turtle as t
import colorsys
import turtle
t.bgcolor("black")
t.tracer(100)
t.pensize(2)
h=0.5
for i in range(250):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h = 0.0008
    t.fillcolor(c)
    t.begin_fill()
    t.fd(i)
    t.ht()
    t.circle(30)
    for j in range(2):
        t.fd(i*j)
        t.rt(109)
        t.end_fill()

#third game
import turtle
import colorama
turtle.draw("body")
turtle.turtle.draw("line")
turtle.bgcolor("black")
turtle.player.draw(blue)
turtle.body_part("head")
turtle.draw("circle")
turtle.draw("eyes")
turtle.draw("oval")
import s2clientprotocol
colorama.draw("pink")
colorama.turtle_draw("greeen")
colorama.draw("clay")
turtle.end()

# fourth game
import turtle
screen = turtle.Screen()
screen.bgcolor("black")

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.speed(2)

player.penup()
player.goto(0, 0)
player.pendown()
player.begin_fill()
player.circle(50)  # Head
player.end_fill()

player.penup()
player.goto(-15, 60)
player.pendown()
player.color("white")
player.begin_fill()
player.circle(5)  # Left eye
player.end_fill()

player.penup()
player.goto(15, 60)
player.pendown()
player.begin_fill()
player.circle(5)  # Right eye
player.end_fill()

player.hideturtle()
turtle.done()




         