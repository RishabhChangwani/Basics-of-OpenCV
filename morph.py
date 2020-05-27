import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('col.jpg',1)
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gblur=cv2.GaussianBlur(grayscaled,(5,5),0)
th=cv2.adaptiveThreshold(gblur,240,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,0.5)
th2=cv2.adaptiveThreshold(grayscaled,240,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,0.5)
m=cv2.morphologyEx(th,cv2.MORPH_DILATE,(5,5))
bf2=cv2.bilateralFilter(m,5,5,5)
bf=cv2.bilateralFilter(th,5,5,5)


#cv2.imshow('Orignal',img)
#cv2.imshow('grayscaled',grayscaled)
#cv2.imshow('gblur',gblur)
cv2.imshow('Adaptive post Blur',th)
#cv2.imshow('Adaptive Pre blur',th2)
#cv2.imshow('Dilate',m)
#cv2.imshow('Gradient',mg)
cv2.imshow('After Bilateral',bf)
cv2.imshow('After Bilateral2',bf2)

cv2.waitKey(0)
cv2.destroyAllWindows()