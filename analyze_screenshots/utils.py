from tensorflow.contrib.keras.api.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from os.path import join


def get_img_for_predict(image_file):
    im = load_img(join(image_file), target_size=(150, 150))
    im = img_to_array(im)
    im = np.expand_dims(im, axis=0)
    im /= 255
    return im


def get_type_of_file(file_name: str):
    return file_name[len(file_name) - 4:len(file_name)]


def get_str_result(res):
    if res >= 0.7:
        return "\nПресъемка"
    elif res <= 0.4:
        return "\nОригинал"
    else:
        return "\nНевозможно точно классифицировать\nвидео"
