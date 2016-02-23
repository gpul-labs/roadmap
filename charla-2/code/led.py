import RPi.GPIO as GPIO # libreria para los GPIO
import time 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) # configurar pin como salida

while 1: # Bucle infinito
  GPIO.output(18, True) # enciende el LED
  time.sleep(1) # aguarda 1 segundo
  GPIO.output(18, False) # apaga el LED
  time.sleep(1) # aguarda 1 segundo
