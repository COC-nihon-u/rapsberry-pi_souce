from RPIO import PWM

servo = PWM.Servo()

servo.set_servo(17,1200)
servo.set_servo(17.2000)

servo.stop_servo(17)

