#!/usr/bin/env python

import RPi.GPIO as GPIO
from socket import *
import cPickle
import time
#GPIO pin assignemtns
RED_OUT=21
YELLOW_OUT=25
GREEN_OUT=12
BLUE_OUT=18

play_colors = [RED_OUT, YELLOW_OUT, GREEN_OUT, BLUE_OUT]

# one time setup
def setup() :
	# use Raspberry Pi board pin numbers
	GPIO.setmode(GPIO.BCM)

	# disable any warnings
	GPIO.setwarnings(False)

	for pin in play_colors :
		print 'output pin ' + str(pin)
		GPIO.setup(pin, GPIO.OUT)

def play(play_list) :
	print 'playing ' + str(play_list)
	for color in play_list :
		GPIO.output(color, GPIO.HIGH)
		time.sleep(1.5)
		GPIO.output(color, GPIO.LOW)
		time.sleep(0.5)
	
	return
		
def receive() :
	s=socket(AF_INET, SOCK_DGRAM)
	s.bind(('',54545))
	m=s.recvfrom(1024)
	print str(m)
	return cPickle.loads(m[0])

try :
	if __name__ == "__main__":
		setup()
		while True:
			r = receive()
			play(r)
except KeyboardInterrupt :
	GPIO.cleanup()

GPIO.cleanup()


