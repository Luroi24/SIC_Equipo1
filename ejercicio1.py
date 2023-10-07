from gpiozero import LED, Button
from time import sleep

verde = LED(17)
amarillo = LED(27)
rojo = LED(22)
boton = Button(2)

while True:
    if boton.is_pressed:
        rojo.off()
        verde.on()
        if boton.is_pressed:
            verde.off()
            amarillo.on()
            if boton.is_pressed:
                amarillo.off()
                rojo.on()