# usb 카메라 테스트

import cv2

# USB 카메라 연결
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    if ret:
        # 그레이스케일 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Threshold 적용
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # 결과 표시
        cv2.imshow('Thresholded Frame', thresh)

        # 'q'를 누르면 루프 탈출
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
