import turtle
from turtle import *
perimetro = 0
acabado = False
i = 1
n = int(input())
begin_fill()
while True:
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