################################################################################
# Name:         Tyler Stevens
# Date:         5/18/2021
# Description:  This program has three modes for the CPX microcontroller.
#               The sound sensor will turn on the 10 neopixels set to a random RGB
#               value, toggling the b button will light up the first of last 5
#               neipixels, and toggling the a button will turn all neopixels to
#               bright red.
#
# Resources:
# sound sensor - https://learn.adafruit.com/make-it-sense/circuitpython-3
#
################################################################################

# imports
import array #convert sample to array, i think
import math #used for mean() method in helper functions
import time #pause infinite loop
from adafruit_circuitplayground.express import cpx #cpx library
from random import randrange #random RGB value
import audiobusio
import board

################################################################################
# This helper function returns normalized root mean square
#
# @param array of values
# @return normilized root mean square
################################################################################
def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )
    return math.sqrt(samples_sum / len(values))

################################################################################
# This helper function returns the mean
#
# @param array of inputs
# @return average of all values in array
################################################################################
def mean(values):
    return sum(values) / len(values)

################################################################################
# This function will us the cpx speaker to play the Darth Vadar theme
#
# @param none
# @return void
################################################################################
def darth_vadar():
    A = 220
    F = 174.61
    C = 130.81
    E = 164.81
    theme =[A,A,A,F,C,A,F,C,A]
    for i in theme:
        print(i)
        cpx.play_tone(i, 0.2)

################################################################################
# This function will light up the first 5 neopixels
#
# @param tuple of RGB color value
# @return void
################################################################################
def frown(color):
    for i in range(0,5):
        cpx.pixels[i]= color

################################################################################
# This function will light up the last 5 neopixels
# mean square
#
# @param none
# @return void
################################################################################
def smile(color):
    for i in range(5,10):
        cpx.pixels[i]= color

################################################################################
# This function sets brightness to full and lights all neopixels to red
# mean square
#
# @param none
# @return void
################################################################################
def alert():
    cpx.pixels.brightness=1
    cpx.pixels.fill((250,0,0))
    print('in alert')

################################################################################
# Main program
#
# Sample sound input infinitly and switch between modes based
# on input from sound sensor and a/b buttons.
#
################################################################################

# constants
RANDOMLIGHT_ON = 300#conditional value for turning on neopixels
BRIGHTNESS = 0.03#default neopixel brightness
SLEEP = 0.4#pause intervals in infinite loop
DEFAULT_COLOR = (247,206,234)

#set up microphone
mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                       sample_rate=16000, bit_depth=16)

#sample array of inputs
samples = array.array('H', [0] * 160)

#dim the lights
cpx.pixels.brightness = BRIGHTNESS

#flag for resting face mode
toggle_face = False

#flag for alert mode
toggle_alert = False

#infinite loop
while True:

    #grab sound
    mic.record(samples, len(samples))

    #get rms from sample array
    magnitude = normalized_rms(samples)

    #print magnitude
    print(((magnitude),))

    #check button a for input
    if cpx.button_a:
        #clear lights
        cpx.pixels.fill(0)

        #negate toggle value
        if toggle_alert == False:
            toggle_alert = True
        else:
            toggle_alert = False
        #rest
        time.sleep(0.1)


    #check button b for input
    if cpx.button_b:
        #clear lights
        cpx.pixels.fill(0)

        #negate toggle value
        if toggle_face == False:
            toggle_face = True
        else:
            toggle_face = False
        #rest
        time.sleep(0.1)


    #choose 3 rand RGB coordinates
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
    elif toggle_alert:
        print('case 2')
        alert()
    #case 3: resting face mode
    else:
        print('case 3')
        cpx.pixels.brightness = BRIGHTNESS
        if toggle_face:
            frown(DEFAULT_COLOR)
        else:
            smile(DEFAULT_COLOR)

#end




