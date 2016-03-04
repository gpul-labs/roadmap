Resumen Charla 2: Introducción a Raspberry Pi
=======

Resumen del Taller/Charla de [@ResonantWave](https://github.com/ResonantWave) en las [GPUL Labs](labs.gpul.org) para realizar la instalación y configuración de una Raspberry Pi, configurar un puente de conexión de red a través de un portátil y aprender a interactuar entre el puerto de conexión GPIO con varios dispositivos electrónicos y sensores.

# Material necesario
- Rapsberry Pi 1 o 2
- Tarjeta SD 4Gb o superior clase 10
- Cable microUSB
- [Cable de red Ethernet cruzado](https://es.wikipedia.org/wiki/RJ-45#Cable_cruzado)
- Portátil con conector RJ45 o adaptador USB a Ethernet RJ45
- Adaptador para tarjetas SD

# 1. Instalación

## 1.1 Instalación del sistema operativo (Raspbian)

Descargar la imagen oficial de [Raspbian](https://www.raspberrypi.org/downloads/raspbian/). Una vez descargada la imagen se pueden realizar los pasos de instalación desde un terminal:
```
# Descomprimir imagen
~$ unzip 2016-02-09-raspbian-jessie.zip

# Insertar y buscar dispositivo de tarjeta SD
~$ sudo fdisk -l | grep mmcblk

# Volcar imagen al dispositivo
~$ sudo dd  bs=4M if=2016-02-09-raspbian-jessie.img of=/dev/mmcblk0 && sync
```

El proceso de escritura puede llevar varios minutos.

## 1.2 Configuración de red

Para acceder al sistema de la Rasberry desde el portátil por [SSH](https://en.wikipedia.org/wiki/Secure_Shell) se puede configurar una conexión compartida entre el equipo y la Raspberry Pi. NetworkManager permite agregar nueva conexión de red cableada y a continuación, en la pestaña "Ajustes de IPv4" seleccionar el método "Compartida con otros equipos".

La IP de la tarjeta de red de la placa se configurará automáticamente a través del protocolo DHCP en cuanto conectemos el cable de red al portátil. Para conocer la IP que se le ha asignado, ejecutar en terminal la siguiente línea de comandos:
```
$ sudo tail -f /var/log/syslog
```
Enchufar el cable de alimentación y de el cable de red y esperar a que la red conecte ambos dispositivos.

En caso de no encontrar la IP, se puede realizar una búsqueda con Nmap:
```
# IP asignada al portátil en el dispositivo Ethernet
~$ ip a sh eth0 | grep inet

# Si la IP del portátil es 192.168.0.10, la red será la 192.168.0.0/24
~$ nmap -PN [IP/Netmask]
# aparecerá una IP con el puerto 22 abierto
```

## 1.3 Manejo básico del sistema

Ahora solo es necesario conectarse a la Raspberry Pi desde un terminal a través de SSH con el usuario pi:
```
~$ ssh pi@[IP]
```
La contraseña por defecto es >! raspberry.

Se puede realizar una actualización de los paquetes:
```
~$ sudo apt-get update && sudo apt-get upgrade -y
```

Cambiar la contraseña de la Raspberry Pi, opción más que recomendable:
```
~$ password
```

Como parte opcional, se puede configurar el acceso SSH mediante par de claves mediante los comandos ssh-keygen y ssh-copy-id.

Para configurar el idioma, expandir la partición del sistema a toda la tarjeta SD o modificar el reloj y los parámetros de memoria RAM asignada a la GPU, entre otros ejecutar el comando:
```
~$ sudo raspi-config
```

# 2. Introducción al GPIO

Una vez se haya accedido al dispositivo ya se puede puede realizar la configuración de GPIO (General-purpose Input/Ouput). La documentación de cada uno de los pines se encuentra disponible en https://es.pinout.xyz.

El fabricante recomienda utilizar como máximo hasta 20mA por cada pin de alimentación y 51mA en total.

Para utilizar la comunicaión con el GPIO desde la línea de comandos hace falta intalar el paquete WiringPi. En Raspbian Jessie este paquete ya está instalado.
```
$ sudo apt-get install wiringpi

# Para activar modo entrada o salida del pin GPIOX
$ gpio -g mode x {out | in}

# Para escribir activar/desactivar el pin GPIOX
$ gpio -g write x {0 | 1}
```

# 3. Ejemplo Led

Se necesitan los siguientes materiales adicionales:
- Protoboard
- Led
- Cables dupont hembra-macho

Conectar un cable de pines dupont a la protoboard con el Led. La parte positiva (ánodo) del Led es la patilla más larga. El cable que conecta con el cátodo (cátodo) del led, conectarlo a uno de los pines GND (tierra) de la placa, por ejemplo el pin 06; y el cátodo a un pin de 5 voltios, por ejemplo al pin GPIO18 (pin número 12).

![Led](https://rawgithub.com/gpul-labs/charla-2/master/images/led.svg)

Para encender el led desde el terminal de la Raspberry Pi solo es necesario indicar que el pin está en modo salida y escribir
```
~$ gpio -g mode 18 out
# Turn on
~$ gpio -g write 18 1
# Turn off
~$ gpio -g write 18 0
```

Para probar a encender y apagar cada segundo descargar y ejecutar el script en Python [led.py](https://github.com/gpul-labs/charla-2/blob/master/code/led.py)

```
~ $ wget https://raw.githubusercontent.com/ResonantWave/charla-2/master/code/led.py
```

El código del script:
```python
#!/usr/bin/env /usr/bin/python

import RPi.GPIO as GPIO # librería para los GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) # configurar pin como salida

while 1: # Bucle infinito
  GPIO.output(18, True) # enciende el LED
  time.sleep(1) # aguarda 1 segundo
  GPIO.output(18, False) # apaga el LED
  time.sleep(1) # aguarda 1 segundo
```

Para ejecutar:
```bash
~$ python led.py
```

Modificar el tiempo de un segundo (time.sleep) a 0.1 segundos y volver a ejecutar el script.

# 4. Sensores I: Switch

Las entradas no admiten más de 3.3v. Los arduinos son de 5v, así que no se deben conectar sin conversor.

El switch tiene una orientación especial, en la parte trasera se ve una línea transversal que indica como colocar en esa posición sobre la protoboard. Colocar los cables de GND y VCC en la columna del switch y a continuación conectar el cable positivo al GPIO23 (pin 16).

![Led](https://rawgithub.com/gpul-labs/charla-2/master/images/tact_switch.svg)

Descargar y ejecutar el script [button.py](code/button.py) del repositorio.

```python
#!/usr/bin/env /usr/bin/python

import RPi.GPIO as GPIO # libreria para los GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP) # configurar pin como entrada con pull-up

while 1: # Bucle infinito
  print(GPIO.input(23)) # lee y muestra el estado del pin
  time.sleep(5) # aguarda medio segundo
```

```
~ $ python button.py
```

# 5. Sensores II: Hall y PIR

## 5.1 Hall

El sensor de efecto Hall es un transductor que varía su tensión de salida en respuesta a un campo magnético. Funciona como un interruptor, si se aplica un campo magnético se mantiene y por el otro se apaga.

```
(Hall)
 ________
/________\
|    |    |
VCC GND OUT
R
10K ohm
```

Conectar el sensor Hall junto con una resistencia de 10K ohmios, tal y como se muesta en la siguiente figura.

![Hall](https://rawgithub.com/gpul-labs/charla-2/master/images/hall.svg)

Ejecutar el script de [hall.py](code/hall.py)
```python
#!/usr/bin/env /usr/bin/python

import RPi.GPIO as GPIO # libreria para los GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN) # configurar pin como entrada

while 1: # Bucle infinito
  if(GPIO.input(18)): # lee el estado del sensor
    print("Sensor hall activado")
  else:
    print("Sensor hall desactivado")
  time.sleep(0.5) # aguarda 1 segundo
```

```bash
$ python hall.py
```

## 5.2 PIR

El sensor PIR (Pasive Infrared sensor) es un sensor electrónico que mide la luz infrarroja y sirve para detectar movimiento.

 ```
(PIR)
  ______
 /      \
 ^|^^|^^|^
GND OUT VCC
```

Conectar el dispositivo PIR, el pines de salida OUT a GPIO18 (pin número 12) y el cable de tierra y alimentación a pines GND y VCC de 5 voltios, tal como se muestra en la figura.

![PIR](https://rawgithub.com/gpul-labs/charla-2/master/images/pir.svg)

Ejecutar el script de [pir.py](code/pir.py)
```python
#!/usr/bin/env /usr/bin/python

import RPi.GPIO as GPIO # libreria para los GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN) # configurar pin como entrada

while 1: # Bucle infinito
  if(GPIO.input(18)): # lee el estado del sensor
    print("El PIR ha detectado movimiento")
  time.sleep(0.5) # aguarda 1 segundo
```

```bash
$ python pir.py
```
