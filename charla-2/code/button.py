import RPi.GPIO as GPIO # libreria para los GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP) # configurar pin como entrada con pull-up

while 1: # Bucle infinito
  print(GPIO.input(23)) # lee y muestra el estado del pin
  time.sleep(5) # aguarda medio segundo
