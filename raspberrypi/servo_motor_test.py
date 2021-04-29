# https://www.explainingcomputers.com/sample_code/Servo_Test_DD_Two_Servos.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Two servos pins 11 & 12
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50)

# Reset
servo1.start(0)
servo2.start(0)

# Turn servo1 to 90
servo1.ChangeDutyCycle(7)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

time.sleep(2)

# Turn servo2 to 90 & servo1 back to 0
servo2.ChangeDutyCycle(7)
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

time.sleep(2)

# Turn servo2 to 180 & servo1 to 90
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(7)
time.sleep(0.5)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

time.sleep(2)

# Turn both servos back to 0
servo2.ChangeDutyCycle(2)
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

time.sleep(2)

servo1.stop()
servo2.stop()
GPIO.cleanup()