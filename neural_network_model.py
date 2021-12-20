#---------------------Training the Model---------

import cv2
import os
import numpy as np

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            images.append(img)
    return images

match = load_images_from_folder("C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Cropped Pretties\\Resized Pretties")
ugly= load_images_from_folder("C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Cropped Uglies\\Resized")

X_match= match
X_ugly=ugly

#creating arrays to assign 1 to Pretty and 0 to Ugly
y_ugly = np.zeros(len(ugly))
y_match = np.ones(len(match))

y= list(y_match)+list(y_ugly)
X= X_match+X_ugly

X=[i/255 for i in X]


#configuring GPU
import tensorflow as tf
config = tf.compat.v1.ConfigProto(log_device_placement=True)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)


#running the model
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense

model = Sequential()
model.add(Conv2D(32,kernel_size=2, input_shape=(450, 450, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32,kernel_size=2))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64,kernel_size=2))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(
        np.array(X), np.array(y),
        epochs=10,
        batch_size=17,
        validation_split=0.2,
        shuffle=True,
        workers=4,
        use_multiprocessing=True)


model.save('model.h5')