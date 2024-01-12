# 영상 픽셀 변경 - 이진화란 영상을 흑/백으로 분류하여 처리하는 것을 말합니다. 
#https://opencv-python.readthedocs.io/en/latest/doc/19.imageHistograms/imageHistograms.html

import cv2
import numpy as np

img = cv2.imread('data/images/hmstory.jpg' , cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image Processing', img)

# ret, img_binary  = cv2.threshold(img,임계값,적용값, cv2.THRESH_BINARY 임계값 넘으면 적용값 반영, 넘지 못하면 0 반영)
ret, img_binary  = cv2.threshold(img,127,255, cv2.THRESH_BINARY)

# 함수는 계산된 최적 임계값(ret)과 이진화된 이미지(img_otsu)를 반환합니다. 자동으로 오츠 알고리즘을 적용하여 최적의 임계값을 계산
ret, img_otsu  = cv2.threshold(img,127,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow('Result_B', img_binary)
cv2.imshow('Result_O', img_otsu)


cv2.waitKey(0)
cv2.destroyAllWindows()
