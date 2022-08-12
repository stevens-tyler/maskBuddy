#################################################################################
# Name:         Tyler Stevens
# Date:         5/18/2021
# Description:  This program uses a CPX microcontroller's sound
#               sensor to turn on the 10 neopixels set to a random RGB value
# Resources:
# sound sensor - https://learn.adafruit.com/make-it-sense/circuitpython-3
#
#
################################################################################


#sound sample source - https://learn.adafruit.com/make-it-sense/circuitpython-3


# imports
import array #convert sample to array, i think
import math #used for mean() method in helper functions
import time #pause infinite loop
from adafruit_circuitplayground.express import cpx #cpx library
from random import randrange #random RGB value
import audiobusio
import board


########################################
# This helper function returns normalized root
# mean square
# @param
# @return
########################################
def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    return math.sqrt(samples_sum / len(values))

########################################
# This helper function
# @param
# @return
########################################
def mean(values):
    return sum(values) / len(values)

########################################
# Main Program
########################################

# constants
RANDOMLIGHT_ON = 300#conditional value for turning on neopixels
REDLIGHT_ON = 600#conditional value for bright red light
BRIGHTNESS = 0.03#default neopixel brightness
SLEEP = 0.4#pause intervals in infinite loop

#set up microphone
mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                       sample_rate=16000, bit_depth=16)

#sample array of inputs
samples = array.array('H', [0] * 160)


#dim the lights
cpx.pixels.brightness = BRIGHTNESS

#infinite loop
while True:
    #grab sound
    mic.record(samples, len(samples))

    #return rms of sound freq
    magnitude = normalized_rms(samples)

    #print magnitude
    print(((magnitude),))
    time.sleep(0.1)


    #choose 3 rand RBG coordinates
    x=randrange(255)
    y=randrange(255)
    z=randrange(255)

    #case 1: speech mode
    if magnitude > RANDOMLIGHT_ON:
        print('case 1')
        cpx.pixels.fill((x, y, z))
        time.sleep(SLEEP)
        cpx.pixels.fill(0)
    #case 2: alert mode
    elif magnitude > REDLIGHT_ON:
        print('case 2')
        cpx.pixels.brightness=1
        cpx.pixels.fill((250,0,0))
        time.sleep(1)
        cpx.pixels.fill(0)
        cpx.pixels.brightness=BRIGHTNESS
    #case 3: smile mode
    else:
        print('case 3')
        for i in range(5):
            cpx.pixels[i]=(247,206,234)







