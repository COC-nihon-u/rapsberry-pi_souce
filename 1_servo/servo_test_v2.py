import webiopi
import time

GPIO = webiopi.GPIO
SERVO_X = 23
DEFAULT_X = 0
CURRENT_X = DEFAULT_X
time_stamp = time.time()

def setup():
    GPIO.setFunction(SERVO_X, GPIO.PWM)
    GPIO.pulseAngle(SERVO_X, DEFAULT_X)
    webiopi.sleep(0.5)
    GPIO.pulseRatio(SERVO_X, 0)

def loop():
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
        GPIO.pulseRatio(SERVO_X, 1)
        GPIO.pulseAngle(SERVO_X, DEFAULT_X)
        webiopi.sleep(0.5)
        GPIO.pulseRatio(SERVO_X, 0)
        webiopi.sleep(0.5)
        time_stamp = time.time()

@webiopi.macro
def left():
    global CURRENT_X, time_stamp
    if CURRENT_X < DEFAULT_X + 5*10 and time_stamp <= time.time() - 0.2:
        GPIO.pulseRatio(SERVO_X, 1)
        time_stamp = time.time()
        CURRENT_X = CURRENT_X + 5
        GPIO.pulseAngle(SERVO_X, CURRENT_X)
        webiopi.sleep(0.5)
        time_stamp = time.time()
        GPIO.pulseRatio(SERVO_X, 0)

@webiopi.macro
def right():
    global CURRENT_X, time_stamp
    if CURRENT_X > DEFAULT_X - 5*10 and time_stamp <= time.time() - 0.2:
        GPIO.pulseRatio(SERVO_X, 1)
        time_stamp = time.time()
        CURRENT_X = CURRENT_X - 5
        GPIO.pulseAngle(SERVO_X, CURRENT_X)
        webiopi.sleep(0.5)
        time_stamp = time.time()
        GPIO.pulseRatio(SERVO_X, 0)

def destroy():
    GPIO.setup(SERVO_X, GPIO.IN)