import cv2
import mediapipe as mp
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

# 시각화 설정
MARGIN = 10  # 픽셀 단위 여백
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)  # 선명한 녹색

# 볼륨 컨트롤을 위한 초기화
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]

# 손 랜드마크 시각화 함수
def draw_landmarks_on_image(rgb_image, detection_result, volume):
    hand_landmarks_list = detection_result.multi_hand_landmarks
    if hand_landmarks_list is None:
        return rgb_image
    annotated_image = np.copy(rgb_image)

    for hand_landmarks in hand_landmarks_list:
        # 손 랜드마크 그리기
        mp.solutions.drawing_utils.draw_landmarks(
            annotated_image,
            hand_landmarks,
            mp.solutions.hands.HAND_CONNECTIONS,
            mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
            mp.solutions.drawing_styles.get_default_hand_connections_style())

        # 엄지와 검지 사이의 막대선 그리기 및 거리 계산
        thumb_tip = hand_landmarks.landmark[4]
        index_finger_tip = hand_landmarks.landmark[8]
        height, width, _ = annotated_image.shape
        x1, y1 = int(thumb_tip.x * width), int(thumb_tip.y * height)
        x2, y2 = int(index_finger_tip.x * width), int(index_finger_tip.y * height)
        cv2.line(annotated_image, (x1, y1), (x2, y2), (255, 0, 0), 5)  # 선 그리기

        # 엄지와 검지 사이의 거리에 따라 볼륨 조절
        distance = math.hypot(x2 - x1, y2 - y1)
        if distance < 50:  # 손가락이 가까울 때 볼륨 0
            volume.SetMasterVolumeLevel(volMin, None)
        else:  # 손가락 사이의 거리에 따라 볼륨 조절
            vol = np.interp(distance, [50, 300], [volMin, volMax])
            volume.SetMasterVolumeLevel(vol, None)

    return annotated_image

# MediaPipe 손 랜드마크 모델 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

# 카메라 캡처 시작
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # BGR 이미지를 RGB로 변환
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 손 랜드마크 감지
    result = hands.process(rgb_frame)

    # 랜드마크 시각화 및 볼륨 조절
    annotated_image = draw_landmarks_on_image(rgb_frame, result, volume)

    # RGB 이미지를 BGR로 변환하여 화면에 표시
    cv2.imshow('Hand Tracking with Volume Control', cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
