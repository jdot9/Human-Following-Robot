import numpy as np
import cv2 as cv
import time
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit


# Below initialises the variable kit to be our I2C Connected Adafruit Motor HAT
kit = MotorKit(i2c=board.I2C())

cap = cv.VideoCapture(0,cv.CAP_V4L)
print("Start Test")
colorDetected = False


if not cap.isOpened():
 print("Cannot open camera")
 exit()
while True:
 # Capture frame-by-frame
 ret, frame = cap.read()
 # if frame is read correctly ret is True
 if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break
 # Our operations on the frame come here
 
 hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 
######## Color detection #########

 upper_red = np.array([180, 255, 255])
 lower_red = np.array([160, 50, 50])
 
 upper_blue = np.array([130, 255, 255])
 lower_blue = np.array([90, 50, 50])
 
 mask = cv.inRange(hsv, lower_blue, upper_blue)
 result = cv.bitwise_and(frame, frame, mask=mask)

 # If color detected, do something
 count = np.sum(np.nonzero(mask))
 #print("count =",count)
 

 if count == 0:
   print("No color found. Searching...")
   colorDetected = False
 else:
   print("Color detected. Following...")
   colorDetected = True
   

#################### Distance Calculation ###################


##################################

 # Display the resulting frame
 #cv.imshow('frame', frame)
 #if cv.waitKey(1) == ord('q'):
  #  break
 

# When everything done, release the capture
#cap.release()
#cv.destroyAllWindows()
