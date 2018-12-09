#Art by ankit

import numpy as np
import cv2
import time
import random

#initialize hight, width for window and number of drope
hight = 1000
width = 1000
num_drops = 500
#choose color's for drops
#color = (255, 0, 0)  #for blue color
#color = (0, 255, 0)  #for green color
color = (0, 0, 255)    #for red color

cap = cv2.VideoCapture(0)

#initialize empty array to store x1, x2, y1, y2, for lines
x1 = np.empty(num_drops)
y1 = np.empty(num_drops)
x2 = np.empty(num_drops)
y2 = np.empty(num_drops)
entry = 0

while(1):
    
    _, img = cap.read()
    #copy the image
    new = img.copy()
    #draw lines for first time
    if (entry == 0):
        entry = 1
        for i in range(num_drops):
            #get random x1, x2, y1, y2
            x1[i] = random.randint(1,width)
            y1[i] = random.randint(1,hight)
            x2[i] = x1[i]
            y2[i] = (y1[i]+random.randint(1,20))
            # Draw a diagonal blue line with thickness of 5 px
            new = cv2.line(new,(int(x1[i]),int(y1[i])),(int(x2[i]),int(y2[i])),blue,3)              
  
    #increase drop's y values so its look like rain
    elif (entry != 0):
        #time.sleep(0.01)
        for i in range(num_drops):
            y1[i] += 35
            y2[i] += 35
            # Draw a diagonal blue line with thickness of 5 px
            new = cv2.line(new,(int(x1[i]),int(y1[i])),(int(x2[i]),int(y2[i])),blue,3)
            #if drops go out to frame
            if (y2[i] > hight):
                y1[i] = random.randint(1,50)
                y2[i] = y1[i] + random.randint(1,20)
                
    #show rain(image)
    cv2.imshow('img', new)
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()
cap.release()

