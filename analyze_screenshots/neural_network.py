from matplotlib import image

import os
import matplotlib.pyplot as plt

from tensorflow.contrib.keras.api.keras.layers \
    import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.contrib.keras.api.keras.models import Sequential
from tensorflow.contrib.keras.api.keras.preprocessing.image import ImageDataGenerator

from analyze_screenshots.utils import get_img_for_predict, get_type_of_file

IMG_HEIGHT = 150
IMG_WIDTH = 150


class Model:
    def __init__(self, epoch):
        self.model = Sequential([
            Conv2D(
                16,
                3,
                padding='same',
                activation='relu',
                input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
            ),
            MaxPooling2D(),
            Conv2D(32, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Conv2D(64, 3, padding='same', activation='relu'),
            MaxPooling2D(),
            Flatten(),
            Dense(512, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        self.history = None

    def load(self, file_name):
        self.model.load_weights('{}.h5'.format(file_name))

    def train(self, train_dir, epochs, batch_size):
        total_train_count = 0
        for dir in train_dir:
            total_train_count += len(os.listdir(dir))

        train_image_generator = ImageDataGenerator(rescale=1. / 255)
        train_data_gen = train_image_generator.flow_from_directory(batch_size=batch_size,
                                                                   directory=train_dir,
                                                                   shuffle=True,
                                                                   target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                                   class_mode='binary')
        self.model.compile(optimizer='adam',
                           loss='binary_crossentropy',
                           metrics=['acc'])

        self.history = self.model.fit_generator(
            train_data_gen,
            steps_per_epoch=total_train_count // batch_size,
            epochs=epochs,
            validation_steps=total_train_count // batch_size
        )

    def save(self, file_name):
        self.model.save_weights('{}.h5'.format(file_name))

    def get_plot(self, epochs):
        acc = self.history.history['acc']
        loss = self.history.history['loss']

        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(range(epochs), acc, label='Training Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(range(epochs), loss, label='Training Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')

        plt.show()

    def testing(self, test_dir, file_name):
        with open("{}.txt".format(file_name), mode='w') as file:
            for img_name in os.listdir(test_dir):
                if get_type_of_file(img_name) == ".png":
                    img = get_img_for_predict(test_dir, image)
                    print('{}  -  {}'.format(image, str(1 - self.model.predict(img)[0, 0])))
                    file.write('{}  -  {}'.format(image, str(1 - self.model.predict(img)[0, 0])))

    def analyse_photo(self, img_path):
        print(img_path)
