from gpiozero import LED, Button

verde = LED(22)
amarillo = LED(14)
rojo = LED(15)

btn = Button(17)

while True:
	if btn.is_pressed:
		rojo.off()
		verde.on()
	if btn.is_pressed:
		verde.off()
		amarillo.on()
	if btn.is_pressed:
		amarillo.off()
		rojo.on()
	
		

