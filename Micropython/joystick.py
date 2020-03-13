'''Este programa es para probar un joystick tipo Elegoo
con la entrada analoga usando transistores para cambiar 
la lectura de un eje a otro creando la ilusion de que 
esta leyendo los dos ejes al mismo tiempo.
Ver detalles en https://github.com/cortatodo/joystick'''

import time
from machine import Pin, ADC

# Pines en esp-8266
D1 = 5 
D2 = 4 
D3 = 0 
D4 = 2 
D5 = 14
D6 = 12
D7 = 13
D8 = 15

# Referencia Entrada Analoga
joy = ADC(0)

# Referencia entradas digitales para hacer pruebas
pinD3 = Pin(D3, Pin.IN) # Boton flash en esp-8266
pinD5 = Pin(D5, Pin.IN, Pin.PULL_UP) # Boton en SW joystick (presionado=0)

# Referencia salidas digitales para alternar bases transistores
pinD1 = Pin(D1, Pin.OUT) # Salida conectada a la base del transistor eje X
pinD2 = Pin(D2, Pin.OUT) # Salida conectada a la base del transistor eje Y

# Referencia variables
t = .01
c = 0
x = 0
y = 0

# Bucle infinito para alternar la lectura de los ejes (X) y (Y)
while True:
	if c == 0:
		pinD1.off()
		pinD2.on()
		time.sleep(t)
		c = 1
		x = joy.read()
	else:
		pinD1.on()
		pinD2.off()
		time.sleep(t)
		c = 0
		y = joy.read()
	print('X: ', x, 'Y: ', y, 'D5 ', pinD5.value())
