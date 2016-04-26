import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)

import time
import os
import sys

prev_input= 1
while True:
	button_input = GPIO.input(17)
	if ((not prev_input) and button_input):
		print 'button ok'
		os.system("sudo python /home/pi/Desktop/leMyope/launchjs.py")
	prev_input = button_input
	time.sleep(0.05)
	sys.exit