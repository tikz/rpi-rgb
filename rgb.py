import time
import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

r = GPIO.PWM(13, 50)
g = GPIO.PWM(6, 50)
b = GPIO.PWM(5, 50)

r.start(0)
g.start(0)
b.start(0)

try:
    while 1:
        for i in range(0, 101, 1):
            r_val = math.sin(2 * math.pi * i/100) * 50 + 50
            print(r_val)
            r.ChangeDutyCycle(r_val)
            time.sleep(0.1)

except KeyboardInterrupt:
    pass

r.stop()
g.stop()
b.stop()
