import cv2

from ml.facial_expression_classification import predict_facial_expression_by_array, IMAGE_WIDTH, IMAGE_HEIGHT
from video.camera import Camera

OPENCV_HAARCASCADE_FRONTALFACE_FILE = 'trained_models/opencv/haarcascades/haarcascade_frontalface_alt.xml'


class EmotionDetectionCamera(Camera):
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(OPENCV_HAARCASCADE_FRONTALFACE_FILE)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        super().__init__()

    def get_frame(self):
        _, frame = self.video.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)

        faces = self.face_cascade.detectMultiScale(frame_gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            face_roi = frame[y:y + h, x:x + w]
            face_roi = cv2.resize(face_roi, (IMAGE_WIDTH, IMAGE_HEIGHT))
            result = predict_facial_expression_by_array(face_roi)

            cv2.rectangle(frame, (x, y - 40), (x + w, y), (0, 255, 0), -1)
            cv2.putText(frame, result, (x + 10, y - 10), self.font, 0.7, (0, 0, 0), 2)

        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
