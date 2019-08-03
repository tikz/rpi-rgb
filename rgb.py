import time
import RPi.GPIO as GPIO
import math

GPIO.setwarnings(False)
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
    while True:
        for i in range(0, 501, 1):
            r_val = math.sin(4 * math.pi * i / 500) * 50 + 50
            g_val = math.sin(6 * math.pi * i / 500) * 50 + 50
            b_val = math.sin(8 * math.pi * i / 500) * 50 + 50
            r.ChangeDutyCycle(r_val)
            g.ChangeDutyCycle(g_val)
            b.ChangeDutyCycle(b_val)
            time.sleep(0.01)

except KeyboardInterrupt:
    pass

r.stop()
g.stop()
b.stop()
