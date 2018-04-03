import RPi.GPIO as GPIO
import time
import datetime
import sqlite3
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)
camera = PiCamera()


def MOTION(PIR_PIN):
    print 'Motion Detected!'
    conn = sqlite3.connect('PiSec.db')
    date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    directory = "/home/pi/PiSec Captures/" + date + ".jpg"
    camera.capture(directory)
    c = conn.cursor()
    c.execute("INSERT INTO Images (ID, ImageDir) VALUES (NULL, ?)", [(directory)])
    conn.commit()
    conn.close()


print 'PiSec Motion Security Activated (CTRL+C to exit)'

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print 'Quit'
    GPIO.cleanup()

