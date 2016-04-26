import os
import time
import sys
import subprocess
import picamera
import ftplib
import urllib
import urllib2
from random import randint

#Record and display picture from camera

camera = picamera.PiCamera()

camera.hflip = True
camera.vflip = True
camera.resolution = (400, 300)

print "camera ok"
camera.capture('/home/pi/Desktop/leMyope/image.jpg')
print "picture taken!"
# os.system("DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority feh --hide-pointer --cycle-once -x -q -D 10 -B black -g 640x480 /home/pi/Desktop/leMyope/image.jpg")

#Upload picture to a FTP
time.sleep(3)
session = ftplib.FTP('[FTP url]','[FTP username]','[FTP password]')
print "logged in"
file = open('/home/pi/Desktop/leMyope/image.jpg','rb')                  # file to send
print "file found"
fileRandomName = 'image' + str(randint(1,1000)) + '.jpg'
fullCommandFileName = 'STOR' + " " + fileRandomName
session.storbinary(fullCommandFileName, file)     # send the file
print "file sent"
file.close()                                    # close file and FTP
session.quit()

#Launch casperjs script from_web.js
CASPERJS_EXECUTABLE = "casperjs" # <-- here you put the path to you casperjs executable
CASPERJS_SCRIPT = "/home/pi/Desktop/leMyope/from_web.js" # this is the name of the script that casperjs should execute
ftpUrl = '[FTP url]'+fileRandomName
googleUrl = 'https://www.google.com/searchbyimage?&image_url='
fullGoogleUrl = googleUrl + ftpUrl

callFeedback = subprocess.call([CASPERJS_EXECUTABLE, CASPERJS_SCRIPT, fullGoogleUrl])
print callFeedback

#Get picture data from txt file and clean data
if callFeedback == 0:
	fo = open("htmlblurb.txt", "r")
	content = fo.read()
	fo.close()
	semiFinalUrl = content[7:(len(content)-1)]
	almostFinalUrl = semiFinalUrl.split('&amp;,imgurl')
	finalUrl = almostFinalUrl[0]
	print finalUrl

#Download Final picture to computer
	pic_in_computer = 'myopePicture1.jpg'
	urllib.urlretrieve(finalUrl, pic_in_computer)
	print 'Success'

#Display picture
	os.system("DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority feh --hide-pointer --cycle-once -x -q -D 10 -B black -g 640x480 myopePicture1.jpg")
	print "Super Prosper !"
	sys.exit()
else:
	print "Gros echec !"
	sys.exit()
