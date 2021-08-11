import base64
import io

import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def visualize(data, titles, xlabels, ylabels):
    fig, axes = plt.subplots(1, len(titles), squeeze=False)
    fig.suptitle('Visualization', fontsize=16)

    for i in range(len(titles)):
        axes[0, i].set_title(titles[i])
        axes[0, i].set_xlabel(xlabels[i])
        axes[0, i].set_ylabel(ylabels[i])

        for s in data[i].keys():
            axes[0, i].plot(data[i][s], label=s)

        axes[0, i].legend(loc="best")
        axes[0, i].grid()

    plt.tight_layout()
    plt.show()


def convert_image_to_base64(img):
    img = Image.open(img).convert('RGB')
    buffered = io.BytesIO()
    img.save(buffered, format="png")
    return base64.b64encode(buffered.getvalue()).decode()


def convert_opencv_image_to_base64(img):
    _, im_arr = cv2.imencode('.png', img)
    im_bytes = im_arr.tobytes()
    return base64.b64encode(im_bytes).decode()


def get_image_with_heatmap_overlay(img, heatmap):
    image = Image.open(img).convert('RGB')
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    heatmap = cv2.resize(heatmap, (image.shape[1], image.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    superimposed_image = heatmap * 0.8 + image

    return superimposed_image
