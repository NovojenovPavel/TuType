import turtle as t
import alphabet

command = str(input())

t.shape("turtle")
t.penup()
t.goto(-350, 0)

alphabet.turtleprint(command,0.5)

int(input())