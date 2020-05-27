import cv2
import numpy as np 


img=cv2.imread("try.png",1)
cv2.imshow('win',img)
cv2.waitKey(0)
cv2.destroyWindow('win')
h=img.shape[0]-1
w=img.shape[1]-1
roi=img[0:500,0:500]
cv2.imshow('win',roi)
cv2.waitKey(0)
cv2.destroyWindow('win')
