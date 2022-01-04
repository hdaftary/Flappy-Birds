import cv2


def detect_face(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    # Draw a ellipse around faces
    faces = face_cascade.detectMultiScale(frame_gray)

    for (x, y, w, h) in faces:
        # color format is BGR. Blue face
        frame = cv2.ellipse(frame, (x + w // 2, y + h // 2), (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

    return faces

def detect_eyes(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    faces = detect_face(frame)
    blinked = False

    if type(faces) != tuple and len(faces) == 1:
        # only one face should be on the screen, that is, only one player should be playing the game
        x_face, y_face, w_face, h_face = faces[0]
        # we will have two eyes
        eyes = eyes_cascade.detectMultiScale(frame_gray[y_face:y_face + h_face, x_face:x_face + w_face])
        for (x_eyes, y_eyes, w_eyes, h_eyes) in eyes:
            eye_center = (x_face + x_eyes + w_eyes // 2, y_face + y_eyes + h_eyes // 2)
            frame = cv2.circle(frame, eye_center, int(round((w_eyes + h_eyes) * 0.25)), (0, 0, 255), 4)  # red eyes

            if eyes is not None:
                blinked = True
            else:
                blinked = False

            cv2.imshow('Capture - Eyes blinked or not', frame)

    return not blinked


def detect_mouth(frame):
    detect_face(frame)
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)

    if len(mouth_rects) == 0:
        mouth_opened = True
    else:
        mouth_opened = False

    for (x, y, w, h) in mouth_rects:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # green color
        break

    cv2.imshow('Capture - Mouth Opened or not', frame)
    return mouth_opened


face_cascade_name = 'assets/cascades/haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_name)

eyes_cascade_name = 'assets/cascades/haarcascade_eye_tree_eyeglasses.xml'  # since I have glasses, used this cascade
eyes_cascade = cv2.CascadeClassifier(eyes_cascade_name)

mouth_cascade_name = 'assets/cascades/haarcascade_mcs_mouth.xml'
mouth_cascade = cv2.CascadeClassifier(mouth_cascade_name)

