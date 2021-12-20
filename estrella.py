from turtle import *
begin_fill()
while True:
    forward(200)
    left(180-45)
    if abs(pos()) < 1:
        break
done()