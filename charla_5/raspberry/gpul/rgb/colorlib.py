#! /usr/bin/env python
#
# Fade an LED (or one color of an RGB LED) using GPIO's PWM capabilities.
#
# Usage:
#   sudo python colors.py 255 255 255
#
# @author Jeff Geerling, 2015

import time
import RPi.GPIO as GPIO

class RgbLed():
    # LED pin mapping and GPIO setup.
    def __init__(self, red=7, green=11, blue=13, mode=GPIO.BOARD):
        GPIO.setmode(mode)
        GPIO.setwarnings(False)

        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)

        # Set up colors using PWM so we can control individual brightness.
        self.red = GPIO.PWM(red, 100)
        self.green = GPIO.PWM(green, 100)
        self.blue = GPIO.PWM(blue, 100)
        self.red.start(0)
        self.green.start(0)
        self.blue.start(0)

    # Set a color by giving R, G, and B values of 0-255.
    def setColor(self, red, green, blue):
        rgb = [red, green, blue]
        # Convert 0-255 range to 0-100.
        rgb = [x / 255.0 * 100 for x in rgb]
        self.red.ChangeDutyCycle(rgb[0])
        self.green.ChangeDutyCycle(rgb[1])
        self.blue.ChangeDutyCycle(rgb[2])
