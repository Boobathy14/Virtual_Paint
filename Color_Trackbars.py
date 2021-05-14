import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def empty():
    pass

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',640,240)
cv2.createTrackbar('Hue Min','Trackbars',0,176,empty)
cv2.createTrackbar('Sat Min','Trackbars',0,255,empty)
cv2.createTrackbar('Val Min','Trackbars',0,255,empty)
cv2.createTrackbar('Hue Max','Trackbars',0,176,empty)
cv2.createTrackbar('Sat Max','Trackbars',0,255,empty)
cv2.createTrackbar('Val Max','Trackbars',0,255,empty)

while True:
    check,img = cap.read()
    #img = cv2.imread('car.jpg')
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min','Trackbars')
    S_min = cv2.getTrackbarPos('Sat Min','Trackbars')
    v_min = cv2.getTrackbarPos('Val Min','Trackbars')
    h_max = cv2.getTrackbarPos('Hue Max', 'Trackbars')
    S_max = cv2.getTrackbarPos('Sat Max', 'Trackbars')
    v_max = cv2.getTrackbarPos('Val Max', 'Trackbars')

    print(h_min,S_min,v_max,h_max,S_max,v_min)
    lower=np.array([h_min,S_min,v_min])
    upper=np.array([h_max,S_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgresult =cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('Original', img)
    cv2.imshow('Mask', mask)
    cv2.imshow('Resuly', imgresult)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    #cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()