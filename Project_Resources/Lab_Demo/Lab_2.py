#-- ExternalProximitySensorWithOutputs.py - CircuitPython code for CPX --#
# Import Section
import board
import pulseio
from adafruit_circuitplayground.express import cpx
from adafruit_hcsr04 import HCSR04
import adafruit_motor.servo
from time import sleep
# Setup Section

sonar = HCSR04(trigger_pin=board.A7, echo_pin=board.A6)
pwm = pulseio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)
# Function Section
def servo_pos(dist):
    dist_min = 5 # Low distance servo [cm]
    dist_max = 50 # High distance servo [cm]
    dist = min((max((dist, dist_min)), dist_max))
    return (((dist-dist_min)/(dist_max-dist_min)) * 180)
# Loop Section
while True:
    try:
        servo.angle = servo_pos(sonar.distance)
        print((sonar.distance, servo.angle))
    except RuntimeError:
        print("Retrying!")
    sleep(0.5)

