#영상을 읽고, 산술 연산 실습
import cv2
import numpy as np

img = cv2.imread('data/images/hmstory.jpg' , cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image Processing', img)


img_plus = cv2.add(img,50, )  #255보다 크면 255으로 자동 조정
img_minus = cv2.subtract(img,50)  #0 보다 작은 0으로 자동 조정
img_mul = cv2.multiply(img,2)
img_div = cv2.divide(img,2)


#img_plus = img + 50   #이것도 가능하나, 0 ~ 255로 변환 필요

img_pp = np.clip(img+50., 0, 255).astype(np.uint8)  # 8비트 부호 없는 정수 형식으로 변환


cv2.imshow('Result_P', img_plus)
cv2.imshow('Result_M', img_minus)
cv2.imshow('Result_Mul', img_mul)
cv2.imshow('Result_D', img_div)
cv2.imshow('Result_PP', img_pp)

cv2.waitKey(0)
cv2.destroyAllWindows()