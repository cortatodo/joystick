# Joystick ESP8266 y Micropython 
Vamos a programar un Joystick Elegoo con Micropython.

<img src='media/Elegoo-joystick.jpg/' width=200 height=200 />

Usando el rete-conocido microcontrolador Nodemcu esp-8266 de Expressiff

<img src='media/NodeMCU-Microncontroller.ppm/' width=300 height=200 />

<a href=https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/>Fotos y pinouts diferentes modelos esp8266 </a> para referencia

Tomado de este excelente blog <a href=https://orionrobots.co.uk/2017/05/28/joystick-attached-to-esp8266.html> Orion Robots</a> y adaptado al espanol para Micropython

EL diagrama basico del joystick es el siguiente.

<img src='media/joystick-innards.png/' style='width:20px;height:20px;'/>

Joystick X y Joystick Y Son dos potenciometros que envian datos analogos al mismo tiempo.
Pero el esp-8266 tiene la limitacion de que solo tiene una entrada analoga (ADC(0))
Una solucion seria usar un esp-32 que tiene 15 entradas analogas.  <a href=https://randomnerdtutorials.com/esp32-adc-analog-read-arduino-ide/>Ver este tutorial</a>

Pero si el microcontrolador que tenemos es esp-8266 pues no tenemos otra opcion que dividir las entradas de cada potenciometro y registrarlas por separado.
Una brillante solucion fue la que encontre en <a href=https://orionrobots.co.uk/2017/05/28/joystick-attached-to-esp8266.html> Orion Robots</a> y funciono a la perfeccion, como mi idioma de programacion favorito es Python, y Micropython decidi hacerlo y subirlo para ustedes.
La configuracion es la misma de las figuras que estan en <a href=https://orionrobots.co.uk/2017/05/28/joystick-attached-to-esp8266.html> Orion Robots</a>.

<h1>Diagrama electronico</h1>
<img src='media/circuit-diagram-fritzing.png/' style='width:20px;height:20px;'/>
<h1>Diagrama bread board</h1>
<img src='media/circuit-breadboard-fritzing.png/' style='width:20px;height:20px;'/>

Elementos usados:

1-Board Nodemcu esp-8266</br>
2-Joystick Elegoo</br>
3-(2) transistores pnp 2n2222</br>
4-(2) resistencias de 2k</br>
5-Bread board</br>
6-Jumpers varios</br>

En mi caso la prueba se hizo con el voltaje suministrado por el USB y solo se uso 3.3v.
