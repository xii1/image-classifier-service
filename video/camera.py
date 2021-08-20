import abc
from abc import ABC

import cv2


class Camera(ABC):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def gen_frames(self):
        while True:
            frame = self.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    @abc.abstractmethod
    def get_frame(self):
        pass
