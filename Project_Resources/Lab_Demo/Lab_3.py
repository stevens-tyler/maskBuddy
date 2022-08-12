#-- ExternalProximitySensorWithWarnings.py - CircuitPython code for CPX --# 5
# Import Section
import board
from adafruit_circuitplayground.express import cpx from adafruit_hcsr04 import HCSR04
from time import sleep
# Setup Section
led_brightness = 0.25
t = 0
dt = 0.25
sonar = HCSR04(trigger_pin=board.A7, echo_pin=board.A6) cpx.pixels.fill((255,0,0))
cpx.pixels.brightness = 0
# Function Section
def pixel_flip():
    if cpx.pixels.brightness > 0:
        cpx.pixels.brightness = 0
    else:
        cpx.pixels.brightness = led_brightness
# Loop Section
while True:
    try:
        d = sonar.distance
        # Closer than 15 cm is Dangerously Close
        if d <=5:
            pixel_flip()
        if t >= 1.0:
            cpx.play_tone(440, 0.25)
    t = 0
    # Closer than 15 cm is Very Close
    elif d <= 15:
        pixel_flip()
# Closer than 30 cm is Close

    elif d <= 30:
        if t >= 1.0:
            pixel_flip()
            t = 0
# Farther than 25 cm is Safe else:
    cpx.pixels.brightness = 0
    print((d,))
    t+=dt
except RuntimeError:
    print("Retrying!")
sleep(dt)

