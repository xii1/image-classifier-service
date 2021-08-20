from flask import Blueprint, Response, render_template

from video.face_detection_camera import FaceDetectionCamera

detector = Blueprint('detector', __name__)


@detector.route('/<handler>', methods=['GET'])
def show(handler):
    return render_template('camera.html', url='handle/' + handler)


@detector.route('/handle/face', methods=['GET'])
def detect_face():
    camera = FaceDetectionCamera()
    return Response(camera.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
