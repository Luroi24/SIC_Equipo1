from gpiozero import LED
from time import sleep  

LED_verde = LED(17)
LED_ambar = LED(27)
LED_rojo = LED(22)

while True:
    Instruccion = input()
    if Instruccion.lower() is "siga":
        LED_verde.on()
        LED_ambar.off()
        LED_rojo.off()

    elif Instruccion.lower() is "precaucion":
        LED_verde.off()
        LED_ambar.on()
        LED_rojo.off()
    elif Instruccion.lower() is "alto":
        LED_verde.off()
        LED_ambar.off()
        LED_rojo.on()
