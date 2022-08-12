#flash RGB
from adafruit_circuitplayground.express import cpx
import time
cpx.pixels.brightness = 0.03
while True:
    cpx.pixels.fill((240, 3, 252))
    time.sleep(0.5)
    cpx.pixels.fill((247, 178, 2))
    time.sleep(0.5)


