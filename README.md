# estrellas_regulares

La **dirección de github** de este repositorio es: [ github](https://github.com/GonzaloGmv/estrellas_regulares)

Este ejercicio consiste en programar una función que dibuje estrellas con un número de puntas dado. 

Para realizar esto, primero he intentado encontrar alguna relación entre el número de vertices y el ángulo, pero no he podido encontrarlo, ni por mis propios medios, ni mediante internet. 

Al no encontrar esto, se me ha ocurrido realizar un bucle que cree la estrella girando 179º y cuando se complete ver el perímetro, y si coincide con el producto del número de vertices y el número de dentro de *forward*, parar, de otro modo, se repetiría este proceso reduciendo 1º. El problema de esto es que tarda demasiado, así que buscando, llegué con una función para que *turtle* fuera más rapido, pero sigue tardando demasiado.

Busqué una manera de que la estrella se dibujara instantaneamente, pero creo que no la hay, así que para evitar gastar mucho tiempo en ver si mi ejercicio funciona, he dejado una captura en la que lo pruebo con 12 vértices y tras 5 minutos de espera, se ejecutó como debís. Siento las molestias.

![estrella_ejecutada](https://user-images.githubusercontent.com/91721237/146821434-82dd9638-96da-4952-be1a-05cf97521cb8.jpg)

Mi **diagrama de flujo** para este proyecto es:

![diagrama_estrella](https://user-images.githubusercontent.com/91721237/146823724-d89996f9-6777-47cf-82ab-75b5b79c2a49.jpg)

El **código** de este proyecto es el siguiente:
```
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
```
