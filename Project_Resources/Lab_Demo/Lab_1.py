#-- ExternalProximitySensor.py - CircuitPython code for CPX --#
# Import Section
import board
from adafruit_hcsr04 import HCSR04
from time import sleep
# Setup Section
sonar = HCSR04(trigger_pin=board.A7, echo_pin=board.A6) # Function Section
# Loop Section
while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    sleep(0.5)
# Write your code here :-)
