import RPi.GPIO as GPIO # libreria para los GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN) # configurar pin como entrada

while 1: # Bucle infinito
  if(GPIO.input(18)): # lee el estado del sensor
    print("El PIR ha detectado movimiento")
  time.sleep(0.5) # aguarda 1 segundo
