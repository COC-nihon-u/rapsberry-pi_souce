#webiopiはpython3で動くので注意

import webiopi
from RPIO import PWM
import time

GPIO = webiopi.GPIO
servo = PWM.Servo()
SERVO_X = 22
LED = 24
DEFAULT_X = 1500
CURRENT_X = DEFAULT_X
time_stamp = time.time()

def setup():
    GPIO.output(SERVO_X, GPIO.LOW)
    GPIO.output(LED, GPIO.LOW)

def loop():
   GPIO.output(LED, True)
   global time_stamp
   if (time_stamp <= time.time() - 20):
       defaultPosition()
   webiopi.sleep(0.5)

@webiopi.macro
def defaultPosition():
    global time_stamp
    if time_stamp <= time.time() - 0.2 and (CURRENT_X != DEFAULT_X):
        time_stamp = time.time()
        global CURRENT_X
        CURRENT_X = DEFAULT_X
        servo.set_servo(SERVO_X, 1500)
        webiopi.sleep(0.5)
        time_stamp = time.time()


@webiopi.macro
def left():
    global CURRENT_X, time_stamp
    if CURRENT_X < DEFAULT_X + 50*10 and time_stamp <= time.time() - 0.2:
        time_stamp = time.time()
        CURRENT_X = CURRENT_X + 100
        servo.set_servo(SERVO_X, CURRENT_X)
        webiopi.sleep(0.5)
        time_stamp = time.time()

@webiopi.macro
def right():
    global CURRENT_X, time_stamp
    if CURRENT_X > DEFAULT_X - 50*10 and time_stamp <= time.time() - 0.2:
        time_stamp = time.time()
        CURRENT_X = CURRENT_X - 100
        servo.set_servo(SERVO_X, CURRENT_X)
        webiopi.sleep(0.5)
        time_stamp = time.time()

servo.set_servo(SERVO_X, DEFAULT_X)
webiopi.sleep(0.5)

def destroy():
    GPIO.digitalWrite(SERVO_X, GPIO.LOW)