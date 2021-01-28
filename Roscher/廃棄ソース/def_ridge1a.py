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
    blur = cv2.blur(image,(2*k+1, 2*k+1))
    cv2.imwrite("smoothed.JPG", image)

    image = Image.open("smoothed.JPG")
    width, height = image.size
    image_data = image.getdata()


    s = np.zeros((height, width),np.uint8)*255
    for x in range(k, width - k):
        print(x)
        for y in range(k, height - k):
            total_r2 = 0.0
            total_g2 = 0.0
            total_b2 = 0.0
            total_r = 0.0
            total_g = 0.0
            total_b = 0.0
            for xx in range(-k, k):
                for yy in range(-k, k):
                    r = image_data[(y + yy) * width + (x + xx)][0]
                    g = image_data[(y + yy) * width + (x + xx)][1]
                    b = image_data[(y + yy) * width + (x + xx)][2]
                    total_r2 += r**2 / 2*k+1
                    total_g2 += g**2 / 2*k+1
                    total_b2 += b**2 / 2*k+1
                    total_r += r / 2*k+1
                    total_g += g / 2*k+1
                    total_b += b / 2*k+1
            total_r = np.sqrt(abs(total_r**2 - total_r2))
            total_g = np.sqrt(abs(total_g**2 - total_g2))
            total_b = np.sqrt(abs(total_b**2 - total_b2))

            #L2 norm
            s[y][x] = int(np.sqrt((total_r**2 + total_g**2 + total_b**2) / 3))
            if s[y][x] > 255:
                print("error : out of 256")
                print(s[y][x])

    cv2.imwrite('S.JPG', s)