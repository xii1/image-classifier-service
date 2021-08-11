from flask import Blueprint, render_template, request

from ml.dog_cat_classification import predict_image
from utils import convert_image_to_base64, get_image_with_heatmap_overlay, convert_opencv_image_to_base64

classifier = Blueprint('classifier', __name__)


@classifier.route('/dogcat', methods=['GET', 'POST'])
def recognize_dog_cat():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        img = convert_image_to_base64(uploaded_file)
        result, heatmaps = predict_image(uploaded_file)

        img_heatmaps = []
        for hm in heatmaps:
            img_hm = get_image_with_heatmap_overlay(uploaded_file, hm)
            img_hm = convert_opencv_image_to_base64(img_hm)
            img_heatmaps.append(img_hm)

        return render_template('result.html', img=img, img_heatmaps=img_heatmaps, message=result)
    return render_template('upload.html', url='dogcat')
