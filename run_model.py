#-----------------Running The Model----------------

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow import keras
from keras.models import load_model, Model
import tensorflow as tf
from PIL import Image
import numpy as np

model=load_model("model.h5")

import os

for x in os.listdir(r"Test Folder"):
    img_pred= tf.keras.preprocessing.image.load_img("Test Folder\" + str(x), target_size=(450,450))
    img_pred= tf.keras.preprocessing.image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred, axis=0)

    result= model.predict(img_pred)
    print('Pic', x, 'is:')

    if result[0][0] == 1:
        prediction= 'Pretty!'
    else:
        prediction= 'Ugly!'

    print(prediction)