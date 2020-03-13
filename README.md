# Joystick ESP8266 y Micropython 
Vamos a programar un Joystick Elegoo con Micropython.

![](Elegoo-joystick.jpg)


<img src='/NodeMCU-Microncontroller.ppm/' style='width:20px;height:20px;'/>

usando el rete-conocido microcontrolador Nodemcu esp-8266 de Expressiff

<a href=https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/>Fotos y pinouts diferentes modelos esp8266 </a> para referencia

Tomado de este excelente blog <a href=https://orionrobots.co.uk/2017/05/28/joystick-attached-to-esp8266.html> Orion Robots</a> y adaptado al espanol para Micropython

EL diagrama basico del joystick es el siguiente.

<img src='/joystick-innards.png/' style='width:20px;height:20px;'/>

Son dos potenciometros que envian datos analogos al mismo tiempo.
Pero el esp-8266 tiene la limitacion de que solo tiene una entrada analoga (ADC(0))
Una solucion seria usar un esp-32 que tiene 15 entradas analogas. Ver .<a href=https://randomnerdtutorials.com/esp32-adc-analog-read-arduino-ide/>aqui</a>
