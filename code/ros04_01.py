import cv2

img = cv2.imread('data/images/bookIcon.png', cv2.IMREAD_COLOR)
cv2.imshow('Image Processing', img)

cv2.waitKey(0)
cv2.destroyAllWindows()