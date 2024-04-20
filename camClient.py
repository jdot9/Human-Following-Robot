import socket
import threading
import time
import numpy as np
import cv2 as cv
from tests import motorTest as mt
from tests import stepperTest as st

FORMAT = 'ascii'
NAME = 'Pi-1'
colorDetected = False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 57599))

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'NAME':
                client.send(NAME.encode(FORMAT))
            else:
                print(message)
        except:
            print("An error occured.")
            client.close()
            break


def write():
    while True:
        message = str(colorDetected)
        if colorDetected:
            client.send(message.encode(FORMAT))
            time.sleep(1)
        else:
            client.send(message.encode(FORMAT))
            time.sleep(1)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

cap = cv.VideoCapture(0)

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
 cv.imshow('frame', result)
 if cv.waitKey(1) == ord('q'):
    break
 

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()