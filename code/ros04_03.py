#컬러 영상을 읽고, 특정 픽셀 값을 읽고, 바꾸어 본다.
import cv2
import numpy as np

img = cv2.imread('data/images/BookIcon.png' , cv2.IMREAD_COLOR)
cv2.imshow('Image Processing', img)

print(img.shape)
px = img[250,250] #바꾸자하는 위치 
print(px) #위 위치의 현재 픽셀값
img[250:260, 250:260] = 0  #특정위치 픽셀값을 검게
img[260:270, 260:270] = [255,255,255]  #특정위치 픽셀값을 밝게  B G R

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()