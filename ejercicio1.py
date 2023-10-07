from gpiozero import LED, Button
from time import sleep

l_verde = LED(17)
l_amarillo = LED(27)
l_rojo = LED(22)
boton = Button(2)

LEDs = [l_verde,l_amarillo,l_rojo]
it = 2

while True:
    if boton.is_pressed:
        LEDs[it].off()          # Apagamos actual
        it+=1                   # Siguiente led
        it = i if i <3 else 0   #Reinicia desde 0 si es edge
        LEDs[it].on()           #Prende el actual