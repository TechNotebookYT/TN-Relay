# Project by: Tech Notebook
# https://bit.ly/35UMJzu

import RPi.GPIO as GPIO
import time

LED = 20

GPIO.setmode(GPIO.BCM)
GPIO.pinmode(LED, GPIO.output)

while True:
    GPIO.output(LED, GPIO.HIGH)
    print("ON")
    time.sleep(2)
    GPIO.output(LED, GPIO.LOW)
    print("OFF")
    time.sleep(2)
# Tech Notebook
# https://bit.ly/35UMJzu
