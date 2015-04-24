import webiopi
import time
import serial

GPIO = webiopi.GPIO
LED = 24
time_stamp = time.time()
ser = serial.Serial('/dev/ttyACM0',9600)

def setup():
    GPIO.output(LED,GPIO.OUT)
    ser.write("c")
    webiopi.sleep(0.5)

def loop():
    GPIO.digitalWrite(LED,True)
    global time_stamp
    if (time_stamp <= time.time() - 20):
       ser.write("c")
    webiopi.sleep(0.5)

@webiopi.macro
def defaultPosition():
    global time_stamp
    if time_stamp <= time.time() - 0.2:
        time_stamp = time.time()
        ser.write("c")

@webiopi.macro
def left():
    global time_stamp
    if time_stamp <= time.time() - 0.2:
        ser.write("b")

@webiopi.macro
def right():
    global time_stamp
    if time_stamp <= time.time() - 0.2:
        ser.write("a")

def destroy():
    GPIO.setup(LED, GPIO.IN)