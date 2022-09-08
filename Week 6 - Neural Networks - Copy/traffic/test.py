import cv2
import numpy as np
import os
import sys


images = []
labels = []
basepath = "C:\\Users\\jgz6\\Downloads\\degrees\\Week 6 - Neural Networks\\traffic\\gtsrb-small"
directory = "gtsrb-small"
for folder in os.scandir(directory):
    #path = os.path.join(basepath, folder)

    for sign in os.scandir(folder):
        image_address = os.path.join(directory, sign)
        image = cv2.imread(image_address, cv2.IMREAD_UNCHANGED)
        image = cv2.resize(image, (30, 30))
        images.append(image)
        labels.append(int(folder.name))
print(images, labels)