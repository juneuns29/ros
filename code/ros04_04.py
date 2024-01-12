#컬러 영상을 읽고, r g b 채널 분리
import cv2
import numpy as np

img = cv2.imread('data/images/hmstory.jpg' , cv2.IMREAD_COLOR)
cv2.imshow('Image Processing', img)


# b, g, r = cv2.split(img)
# img = cv2.merge((b,g,r))
# split() 함수보다 numpy indexing이 빠르다

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

cv2.waitKey(0)
cv2.destroyAllWindows()