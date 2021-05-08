from tensorflow.contrib.keras.api.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from os.path import join

from analyze_screenshots.neural_network import IMG_HEIGHT, IMG_WIDTH


def get_img_for_predict(image_file):
    im = load_img(join(image_file),
                  target_size=(IMG_HEIGHT, IMG_WIDTH))
    im = img_to_array(im)
    im = np.expand_dims(im, axis=0)
    im /= 255
    return im


def get_type_of_file(file_name: str):
    return file_name[len(file_name) - 4:len(file_name)]


def get_str_result(res):
    if res >= 0.7:
        return "Кадр из видео, являющегося пересъемкой"
    elif res <= 0.4:
        return "Кадр из видео, являющегося оригиналом"
    else:
        return "Невозможно точно классифицировать видео"
