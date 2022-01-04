import cv2
import speech_recognition as sr


def face_detection():
    face_cascade_name = 'assets/cascades/haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_name)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)

        # -- Detect faces
        faces = face_cascade.detectMultiScale(frame_gray)
        for (x_face, y_face, w_face, h_face) in faces:
            center = (x_face + w_face // 2, y_face + h_face // 2)
            frame = cv2.ellipse(frame, center, (w_face // 2, h_face // 2), 0, 0, 360, (255, 0, 0),
                                4)  # color format is BGR. blue faces

        cv2.imshow('frame', frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def mouth_open_detection():
    mouth_cascade_name = 'assets/cascades/haarcascade_mcs_mouth.xml'
    mouth_cascade = cv2.CascadeClassifier(mouth_cascade_name)
    cap = cv2.VideoCapture(0)
    ds_factor = 0.5

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (600, 600), fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
        for (x, y, w, h) in mouth_rects:
            y = int(y - 0.15 * h)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            break

        cv2.imshow('Mouth Detector', frame)

        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def eye_blink_detection():
    face_cascade_name = 'assets/cascades/haarcascade_frontalface_alt.xml'
    eyes_cascade_name = 'assets/cascades/haarcascade_eye_tree_eyeglasses.xml'  # since I have glasses, used this cascade

    face_cascade = cv2.CascadeClassifier(face_cascade_name)
    eyes_cascade = cv2.CascadeClassifier(eyes_cascade_name)

    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            eyes = eyes_cascade.detectMultiScale(roi_gray)
            for (x_eyes, y_eyes, w_eyes, h_eyes) in eyes:
                eye_center = (x + x_eyes + w_eyes // 2, y + y_eyes + h_eyes // 2)
                radius = int(round((w_eyes + h_eyes) * 0.25))
                cv2.circle(img, eye_center, radius, (0, 0, 255), 4)  # red eyes

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def voice_to_text_using_google():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Tell us something")
            audio = r.listen(source)
        try:
            speech = r.recognize_google(audio)
            print("You have said " + speech)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


if __name__ == '__main__':
    # mouth_open_detection()
    # eye_blink_detection()
    face_detection()
