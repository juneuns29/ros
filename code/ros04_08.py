import cv2

def cartoonize_image(img, ksize=5, sketch_mode=False):
    # 이미지를 단순화하기 위해 bilateral 필터 적용
    img_color = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # 경계선을 강조하기 위해 그레이스케일로 변환하고, 메디안 블러 적용
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)

    # 경계선 검출을 위해 adaptiveThreshold 사용
    img_edge = cv2.adaptiveThreshold(img_blur, 255, 
                                     cv2.ADAPTIVE_THRESH_MEAN_C, 
                                     cv2.THRESH_BINARY, 
                                     blockSize=9, 
                                     C=2)

    # 경계선을 컬러 이미지에 적용
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
    img_cartoon = cv2.bitwise_and(img_color, img_edge)

    # 스케치 모드
    if sketch_mode:
        return cv2.cvtColor(img_blur, cv2.COLOR_GRAY2BGR)

    return img_cartoon

# USB 카메라 캡처 시작
cap = cv2.VideoCapture(0)

# 카메라가 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    # 카메라 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다. 종료합니다.")
        break

    # 이미지를 만화 스타일로 변환
    cartoon_frame = cartoonize_image(frame)

    # 변환된 이미지 보여주기
    cv2.imshow('Cartoon Camera', cartoon_frame)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 캡처 종료
cap.release()
cv2.destroyAllWindows()