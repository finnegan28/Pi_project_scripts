import RPi.GPIO as GPIO
import time
import datetime
import sqlite3
from picamera import PiCamera
import gcloud
from pyfcm import FCMNotification
from firebase import firebase
from urllib2 import urlopen

my_ip = urlopen('http://ip.42.pl/raw').read()
GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)
camera = PiCamera()
firebase = firebase.FirebaseApplication('https://pisec-662475.firebaseio.com/')
UID = 'wlQ1tt056jWznyszDGj3cNUo7GD3'

Token = firebase.get('users/' + UID + '/token', None)


def MOTION(PIR_PIN):
    for x in xrange(1, 3, 1):
        date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        directory = "/var/www/html/PiSec Captures/" + date + "_Shot%d.jpg" % (x)
        url = "http://" + my_ip + "/PiSec%20Captures/" + date + "_Shot%d.jpg" % (x)
        camera.capture(directory)
        print 'Image Captured %d' % (x)
        firebase.post('users/%s/images' % UID, url)
        time.sleep(1)
    pushNotification()


def pushNotification():
    push_service = FCMNotification(
        api_key="")
    registration_id = Token
    message_title = 'Motion Detected!'
    message_body = 'View Alert'
    sound = 'default'
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body, sound=sound)


print 'PiSec Security System (CTRL+C to exit)'

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        time.sleep(0.5)
except KeyboardInterrupt:
    print 'Quit'
    GPIO.cleanup()
