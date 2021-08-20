import cv2

from video.camera import Camera

OPENCV_HAARCASCADE_FRONTALFACE_FILE = 'trained_models/opencv/haarcascades/haarcascade_frontalface_alt.xml'
OPENCV_HAARCASCADE_EYE_FILE = 'trained_models/opencv/haarcascades/haarcascade_eye_tree_eyeglasses.xml'


class FaceDetectionCamera(Camera):
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(OPENCV_HAARCASCADE_FRONTALFACE_FILE)
        self.eye_cascade = cv2.CascadeClassifier(OPENCV_HAARCASCADE_EYE_FILE)
        super().__init__()

    def get_frame(self):
        _, frame = self.video.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)

        faces = self.face_cascade.detectMultiScale(frame_gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            faceROI = frame_gray[y:y + h, x:x + w]
            eyes = self.eye_cascade.detectMultiScale(faceROI, 1.3, 5)
            for (x_e, y_e, w_e, h_e) in eyes:
                cv2.rectangle(frame, (x + x_e, y + y_e), (x + x_e + w_e, y + y_e + h_e), (0, 0, 255), 3)

                eye_center = (x + x_e + w_e // 2, y + y_e + h_e // 2)
                radius = int(round((w_e + h_e) * 0.25))
                cv2.circle(frame, eye_center, radius, (255, 0, 0), 3)

        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
