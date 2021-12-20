import turtle
from turtle import *
perimetro = 0
acabado = False
i = 1
n = int(input("Introduzca el numero de vertices que quiere que tenga la estrella: "))
begin_fill()
while True:
    turtle.speed('fastest')
    forward(200)
    left(180-i)
    perimetro = perimetro + 200
    if abs(pos()) < 1:
        if perimetro == 200 * n:
            break
        else:
            i = i + 1
            turtle.reset()
            perimetro = 0
done()