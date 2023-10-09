from gpiozero import LED
 

LED_verde = LED(17)
LED_ambar = LED(27)
LED_rojo = LED(22)

while True:
    Instruccion = input()
    if Instruccion.lower() == "siga":
        LED_verde.on()
        LED_ambar.off()
        LED_rojo.off()

    elif Instruccion.lower() == "precaucion":
        LED_verde.off()
        LED_ambar.on()
        LED_rojo.off()
    elif Instruccion.lower() == "alto":
        LED_verde.off()
        LED_ambar.off()
        LED_rojo.on()
