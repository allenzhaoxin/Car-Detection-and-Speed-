import cv2
import numpy as np
import os
import time
import pandas as pd

cascade_src = 'cars.xml'
video_src = 'new.mp4'
cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
i=0
ret, img = cap.read()
while ret:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clone=img.copy()
    cars = car_cascade.detectMultiScale(gray, 2, 1)
    for (x,y,w,h) in cars:
        if w>300:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            crop_img=clone[y:y+h,x:x+w]
            i=i+1
            name='pics\pic'+str(i)+'.png'
            cv2.imwrite(name,crop_img)
            cv2.imshow("crop",crop_img)

     
    cv2.imshow('video', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    ret, img = cap.read()

cv2.destroyAllWindows()
