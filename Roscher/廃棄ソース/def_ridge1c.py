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
    mI2 = np.zeros((height, width, channels))
    s = np.zeros((height, width),np.uint8)*255
    sm = np.zeros((height, width),np.uint8)*255
    sm2 = np.zeros((height, width),np.uint8)*255

    for z in range(channels):
        for y in range(width):
            for x in range(height):
                mI2[x][y][z] = image[x, y, z]**2
    smoothed2 = cv2.blur(mI2,(2*k+1, 2*k+1))


    for x in range(height):
        for y in range(width):
            sm[x][y] = np.sqrt((smoothed[x][y][0]**2 + smoothed[x][y][1]**2 + smoothed[x][y][2]**2) / 3)
            sm2[x][y] = np.sqrt((smoothed2[x][y][0]**2 + smoothed2[x][y][1]**2 + smoothed2[x][y][2]**2) / 3)


    print("smoothed complete")
    

    for x in range(height):
        for y in range(width):
            s[x][y] = int(abs(sm2[x][y] - sm[x][y]))
            print(s[x][y])
            if s[x][y] > 255:
                print(s[x][y])

    cv2.imwrite('S.jpg', s)