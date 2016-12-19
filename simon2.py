#!/usr/bin/python

# Author: Sydney Newshel
# Description: This application works with the bread board to play simon
#
# Updates ---
# Summer 2016 - Initial Application (Predicate Academy Class)
# 12/xx/2016 - Added x

from gpiozero import LED, Button
import time, random

# - LEDs - blue, yellow, green, red
lights = [LED(18), LED(25), LED(12), LED(21)]

# - input buttons
buttons = [Button(22, pull_up=True, bounce_time=0.01),
           Button(13, pull_up=True, bounce_time=0.01),
           Button(19, pull_up=True, bounce_time=0.01),
           Button(26, pull_up=True, bounce_time=0.01)]

# - button event callbacks
buttons[0].when_pressed = lambda x : button_press(lights[0])
buttons[1].when_pressed = lambda x : button_press(lights[1])
buttons[2].when_pressed = lambda x : button_press(lights[2])
buttons[3].when_pressed = lambda x : button_press(lights[3])

# - capture list for user input
capture = []

# - pick a random color
def pick() :
    return lights[random.randrange(0,4)]

# - flash each light in the list
def play(play_list) :
    for light in play_list :
        flash(light, 1.0)
	time.sleep(0.5)
	
# - generic flash function
def flash(light, delay) :
    light.on()
    time.sleep(delay)
    light.off()

# - test user input against play list
def record(round, play_list) :
    while len(capture) < round :
	for x in range(len(play_list)) :
	    if x < len(capture) :
		if play_list[x] != capture[x] :
		    print 'fail 1'
		    return False
	time.sleep(0.1)

    if len(capture) != len(play_list) :
	print 'fail 2'
	return False

    for x in range(len(play_list)) :
	if play_list[x] != capture[x] :
	    print 'fail 3'
	    return False	

    return True

# - event callback when a button is pressed
def button_press(light):
    global capture
    print str(light.pin)
    flash(light, 0.1)
    capture.append(light)

# - what to happen when the user looses
def fail() :
    for x in range(10) :
	for light in lights :
            light.on()
	time.sleep(0.1)
	for light in lights :
            light.off()
	time.sleep(0.1)

# - the main loop
def main() :
    play_list = []
    round = 1
    while True:
    	print 'round ' + str(round)
    	play_list.append(pick())
    	play(play_list)
    	global capture
    	capture = []
    	status = record(round, play_list)
    	if status == False :
	    fail()
            round = 0
	    play_list = []
	time.sleep(2)
	round = round + 1

if __name__ == "__main__":
    main()
