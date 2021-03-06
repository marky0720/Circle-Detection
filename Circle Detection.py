import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    blur = cv2.medianBlur(gray,5)
    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1.5,10)
    
    try:
        
        for i in circles[0,:]:
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),5)
            cv2.putText(frame,str(len(circles[0])-1),(10,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)

        cv2.imshow('Detected Circle', frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
            
    except:
        
        cv2.imshow('No Circle', frame)
        
cam.release()
cv2.destroyAllWindows()