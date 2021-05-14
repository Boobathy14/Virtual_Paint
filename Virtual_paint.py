import cv2
import numpy as np

cap=cv2.VideoCapture(0)

colors=[[38,158,87,87,255,255],
       [0,95,193,80,255,255]]

pointcolor=[[15,190,5],
            [5,250,236]]

drawpoint=[] #x,y,pointcolor

def color_Pick(img,colors,pointcolor):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count =0
    newpoints = []
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getcontours(mask)
        cv2.circle(testimg, (x, y), 12, pointcolor[count], cv2.FILLED)
        if x != 0 and y != 0:
            newpoints.append([x, y, count])
        count += 1
        #cv2.imshow(str(color[0]),mask)
    return newpoints

def getcontours(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cont in contours:
        area =cv2.contourArea(cont)
        if area>500:
            #cv2.drawContours(testimg, contours, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cont,True)
            approx = cv2.approxPolyDP(cont,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y #Used to mark the point at the top center

def draw_it(drawpoint,pointcolor):
    for point in drawpoint:
        cv2.circle(img, (point[0], point[1]), 12, pointcolor[point[2]], cv2.FILLED)

while True:
    check, img = cap.read()
    testimg = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 30, 100)
    newpoints = color_Pick(img, colors, pointcolor)
    if len(newpoints) != 0:
        for newP in newpoints:
            drawpoint.append(newP)
        if len(drawpoint) != 0:
            draw_it(drawpoint, pointcolor)
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()