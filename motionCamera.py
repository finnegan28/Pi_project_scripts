import RPi.GPIO as GPIO
import time
import datetime
import sqlite3
from picamera import PiCamera
import gcloud
from pyfcm import FCMNotification
from firebase import firebase

GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)
camera = PiCamera()
firebase = firebase.FirebaseApplication('https://pisec-662475.firebaseio.com/')


def MOTION(PIR_PIN):
    for x in xrange(1, 3, 1):
        date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        directory = "/var/www/html/PiSec Captures/" + date + " Shot %d.jpg" % (x)
        url = "http://92.13.238.188/PiSec%20Captures/" + date + " Shot %d.jpg" % (x)
        camera.capture(directory)
        print 'Image Captured %d' % (x)
        time.sleep(1)
        firebase.post('/images', url)
    pushNotification()


def pushNotification():
    push_service = FCMNotification(
        api_key="AAAATLrII80:APA91bFUNORsR6DydimlmLF1czI3xKt-yVHhwVK0i22s1B-e1ggNszmaZB29f2ACwJhn7xdiLIWMQG5DNZbZxcuIyuEQ37IStxJivtHttRovz3I6W_ldvkNlvXfnbz9j6IFIcdPLZ_Dm")
    registration_id = "eZBi5oJvcJI:APA91bE_VPHC8NOXFzwkNttdVrRujCQJZKnHmTqQGUMcc96_l7oB2NWlkzpwnGORfv6MGsEKGG6ov68mvWfeQaYF6B14sctu7e9x1JakBGBrPBSAANU2U2zLT_O0pGNV0mPaeFEnp8CN"
    message_title = 'Motion Detected!'
    message_body = 'Motion Detected!'
    sound = 'default'
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body, sound=sound)


print 'PIR Module Test (CTRL+C to exit)'

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        time.sleep(0.5)
except KeyboardInterrupt:
    print 'Quit'
    GPIO.cleanup()
