#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text= input('Write data what you want to write on card ')
    reader.write(text)
    print("Data was writen on card")

finally:
    GPIO.cleanup()
    
