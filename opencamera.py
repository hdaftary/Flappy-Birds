# use camera to detect eye blink or mouth open
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened:
    print('Error opening video camera, please connect a webcam')
    exit(0)
