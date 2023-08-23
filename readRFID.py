#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
#from LEDS import GPIOValues


try:
    reader = SimpleMFRC522()
    while True:
        try:
            id, text= reader.read()
            print(id)
            print(text)
            # gpins = GPIOValues()
            # gpins.defaultPinsValues()

            # #gpins.beepShine(21,17)
            # gpins.shine(21)
            # #gpins.shine(12)
            # gpins.defaultPinsValues()
        
       

        finally:
            GPIO.cleanup()
except KeyboardInterrupt:
    print('interrupted!')

    
