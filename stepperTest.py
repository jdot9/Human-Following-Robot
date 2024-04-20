
import time
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

# Energised Motors get HOT over time along with the electronic silicon drivers
# Below initialises the variable kit to be our I2C Connected Adafruit Motor HAT
kit = MotorKit(i2c=board.I2C())

def search():
    # Look left
    for i in range(50):
        kit.stepper2.onestep()
        time.sleep(0.01)
        
    # Look right
    for i in range(100):
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)  

    # Look Forward
    for i in range(50):
        kit.stepper2.onestep()
        time.sleep(0.01)

    # Look Up
    for i in range(20):
        kit.stepper1.onestep()
        time.sleep(0.01)

    time.sleep(.5)

    # Look Left
    for i in range(50):
        kit.stepper2.onestep()
        time.sleep(0.01)

    # Look Right
    for i in range(100):
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)  

    # Look Forward
    for i in range(50):
        kit.stepper2.onestep()
        time.sleep(0.01)

    # Look down (Return to original location)
    for i in range(20):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)  

    # De-energise stepper motors
    kit.stepper1.release()   
    kit.stepper2.release()

search()