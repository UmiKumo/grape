#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
#import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
import math

def standard_deviation(image_name, k):
    image = cv2.imread(image_name)
    image = cv2.blur(image,(2*k+1, 2*k+1))
    cv2.imwrite("smoothed.JPG", image)

    image = Image.open("smoothed.JPG")
    width, height = image.size
    copy_data = image.getdata()

    image_data = []
    for y in range(height):
        for x in range(width):
            r = copy_data[y * width + x][0]
            g = copy_data[y * width + x][1]
            b = copy_data[y * width + x][2]
            image_data.append(int(np.sqrt((r**2 + g**2 + b**2) / 3)))


    s = np.zeros((height, width),np.uint8)*255
    for x in range(k, width - k):
        print(x)
        for y in range(k, height - k):
            total_2 = 0.0
            total = 0.0
            for xx in range(-k, k):
                for yy in range(-k, k):
                    pixel = image_data[(y + yy) * width + (x + xx)]
                    total_2 += pixel**2 / 2*k+1
                    total += pixel / 2*k+1

            s[y][x] = int(np.sqrt(abs(total**2 - total_2)))
            if s[y][x] > 255:
                print("error : out of 256")
                print(s[y][x])

    cv2.imwrite('S.JPG', s)