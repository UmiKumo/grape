#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
#import matplotlib.pyplot as plt
import numpy as np
import cv2
import math

def standard_deviation(image_name, k):
    image = cv2.imread(image_name)
    smoothed = cv2.blur(image,(2*k+1, 2*k+1))
    height, width, channels = image.shape[:3]
    #mI2 = [[[0] * channels for i in range(height)] for j in range(width)]
    smoothed2 = np.zeros((height, width, channels))
    s = np.zeros((height, width),np.uint8)*255

    for z in range(channels):
        for y in range(width):
            for x in range(height):
                smoothed2[x][y][z] = image[x, y, z]**2
    smoothed2 = cv2.blur(smoothed2,(2*k+1, 2*k+1))


    print("smoothed complete")
    

    for x in range(height):
        print(x)
        for y in range(width):
            r = np.sqrt(abs(smoothed2[x][y][0] - image[x][y][0]**2))
            g = np.sqrt(abs(smoothed2[x][y][1] - image[x][y][0]**2))
            b = np.sqrt(abs(smoothed2[x][y][2] - image[x][y][0]**2))

            #L2 norm
            s[x][y] = int(np.sqrt((r**2 + g**2 + b**2) / 3))
            if s[x][y] > 255:
                print(s[x][y])

    cv2.imwrite('S.JPG', s)