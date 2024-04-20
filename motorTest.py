import time
import board
from adafruit_motorkit import MotorKit

# Initialises the variable kit to be our I2C Connected Adafruit Motor HAT. 
kit = MotorKit(i2c = board.I2C())

# Turn 180 degrees (Clockwise) 1.7
def rotateCW180():
    kit.motor1.throttle = -1
    kit.motor2.throttle = -1
    kit.motor3.throttle = 1
    kit.motor4.throttle = 1
    time.sleep(1.7)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = None
    kit.motor2.throttle = None
    kit.motor3.throttle = None
    kit.motor4.throttle = None

# Turn 360 degrees (Clockwise) 3.4
def rotateCW360():
    kit.motor1.throttle = -1
    kit.motor2.throttle = -1
    kit.motor3.throttle = 1
    kit.motor4.throttle = 1
    time.sleep(3.4)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = None
    kit.motor2.throttle = None
    kit.motor3.throttle = None
    kit.motor4.throttle = None

# Turn 180 degrees (Clockwise) 1.7
def rotateCCW180():
    kit.motor1.throttle = 1
    kit.motor2.throttle = 1
    kit.motor3.throttle = -1
    kit.motor4.throttle = -1
    time.sleep(1.7)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = None
    kit.motor2.throttle = None
    kit.motor3.throttle = None
    kit.motor4.throttle = None

# Turn 360 degrees (Clockwise) 3.4
def rotateCCW360():
    kit.motor1.throttle = 1
    kit.motor2.throttle = 1
    kit.motor3.throttle = -1
    kit.motor4.throttle = -1
    time.sleep(3.4)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = None
    kit.motor2.throttle = None
    kit.motor3.throttle = None
    kit.motor4.throttle = None

def moveForward(x):
    kit.motor1.throttle = 1
    kit.motor2.throttle = 1
    kit.motor3.throttle = 1
    kit.motor4.throttle = 1
    time.sleep(x)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = None
    kit.motor2.throttle = None
    kit.motor3.throttle = None
    kit.motor4.throttle = None

def moveBackward(x):
    kit.motor1.throttle = -1
    kit.motor2.throttle = -1
    kit.motor3.throttle = -1
    kit.motor4.throttle = -1
    time.sleep(x)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = None
    kit.motor2.throttle = None
    kit.motor3.throttle = None
    kit.motor4.throttle = None

def turnRight():
    kit.motor1.throttle = -1
    kit.motor2.throttle = -1
    kit.motor3.throttle = 1
    kit.motor4.throttle = 1
    time.sleep(1)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = None
    kit.motor2.throttle = None
    kit.motor3.throttle = None
    kit.motor4.throttle = None

def turnLeft():
    kit.motor1.throttle = 1
    kit.motor2.throttle = 1
    kit.motor3.throttle = -1
    kit.motor4.throttle = -1
    time.sleep(1)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = None
    kit.motor2.throttle = None
    kit.motor3.throttle = None
    kit.motor4.throttle = None


turnLeft()



    
