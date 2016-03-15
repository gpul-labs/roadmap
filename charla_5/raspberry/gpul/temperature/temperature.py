#!/usr/bin/env python2
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import sys
import requests
import socket
import urllib.parse
from uuid import getnode as get_mac
import atexit

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

LED = 24
GPIO.setup(LED, GPIO.OUT)

def ledOn():
    GPIO.output(LED, True)

@atexit.register
def ledOff():
    GPIO.output(LED, False)

hostname = socket.gethostname()
mac = get_mac()
address = sys.argv[1]
address = urllib.parse.urljoin(address, '/core/postData/')
print('Posting data to', address)


instance = dht11.DHT11(pin=23)
ledOff()

while True:
    result = instance.read()
    if result.is_valid():
        ledOn()
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        ledOff()
        requests.post(address, json={'device': {'mac': mac, 'hostname': hostname}, 'data': {'name': 'Temperature', 'value': result.temperature}})
        ledOn()
        ledOff()
        requests.post(address, json={'device': {'mac': mac, 'hostname': hostname}, 'data': {'name': 'Humidity', 'value': result.humidity}})
        ledOn()

    time.sleep(1)
