import RPi.GPIO as GPIO
import time
import datetime
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)
camera = PiCamera()
date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

def MOTION(PIR_PIN):
    print 'Motion Detected!'
    camera.capture("/home/pi/PiSec Captures/" + date + ".jpg")

print 'PIR Module Test (CTRL+C to exit)'

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print 'Quit'
    GPIO.cleanup()
