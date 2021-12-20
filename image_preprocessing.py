# -------------------Image Pre-Processing--------------------------------------------

import cv2
import numpy as np
import sys
import dlib
import os
import imutils
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from PIL import Image

# renaming pictures in order to be able to loop them in the OpenCV step
path = "C:\\Users\\Zoe Mercury\\Desktop\\Test Batch"
files = os.listdir(path)
destination = "C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Test"

i = 0
for file in files:
    i += 1
    os.rename(path + '\\' + file, destination + '\\' + "IMG" + str(i) + '.jpg')

# Locate into folder where 'haarcasacades' is
os.getcwd()
os.listdir()
os.chdir(r'C:\Users\Zoe Mercury\Desktop\Iron\Final Project\Code\Tutorials\opencv\data\haarcascades')

# Initiate Cascade
imagePath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(
    "C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Code\\Tutorials\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml")

for i in range(1, 82):
    # Read the image
    image = cv2.imread(
        "C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Test\\IMG" + str(i) + ".jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.6,
        minNeighbors=10,
        minSize=(100, 100))

    # Draw a rectangle around the faces & save locally
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = image[y:y + h, x:x + w]
        print("Object found. Saving locally.")
        cv2.imwrite(str(i) + '.jpg', roi_color)

    # since he doesn't catch all faces, we need to rename once more, so that there
# is a sequence of numbers when we try to loop

path = "C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Code\\Tutorials\\opencv\\data\\haarcascades"
files = os.listdir(path)
destination = "C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Test Faces"
i = 1
for file in files[:36]:
    i += 1
    os.rename(path + '\\' + file, destination + '\\' + str(i) + '.jpg')

# Changing Directory in order to save files in desired folder
os.getcwd()
os.listdir()
os.chdir('C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Test Faces')

# resizing pictures while preserving ratio
for i in range(2, 37):
    image = cv2.imread(
        "C:\\Users\\Zoe Mercury\Desktop\\Iron\\Final Project\\Jose Matches\\Test Faces\\" + str(i) + ".jpg")

    resized = imutils.resize(image, width=450)
    cv2.imwrite(str(i) + '.jpg', resized)
    cv2.waitKey(0)

# resizing without preserving ratio
for i in range(2, 38):
    image = cv2.imread(
        "C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Test Faces\\" + str(i) + ".jpg")
    resized = cv2.resize(image, (450, 450))
    cv2.imwrite(str(i) + '.jpg', resized)
    cv2.waitKey(0)

# looping through all pics in Folder, turning into PIL and saving 5 distorted pics of it into data_aug
datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0,
    height_shift_range=0,
    rescale=1. / 255,
    shear_range=10,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

for n in range(2, 38):
    img = Image.open(
        "C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Test Faces\\" + str(n) + ".jpg")
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir="C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Test Faces\\",
                              save_prefix='str(i)', save_format='jpg'):
        i += 1
        if i > 5:
            break

# rename one last time
path = "C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Test Faces"
files = os.listdir(path)
destination = "C:\\Users\\Zoe Mercury\\Desktop\\Iron\\Final Project\\Jose Matches\\Final"

i = 0
for file in files:
    i += 1
    os.rename(path + '\\' + file, destination + '\\' + str(i) + '.jpg')