#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

def standard_deviation(image_name, k):
    image = cv2.imread(image_name)
    average = cv2.blur(image,(2*k+1, 2*k+1))
    height, width, channels = image.shape[:3]
    s = np.zeros((height, width),np.uint8)*255

    for x in range(k, height - k):
        if x%100 == 0:
            print(x)
        for y in range(k, width - k):
            r = np.sqrt(abs(average[x][y][0]**2 - image[x][y][0]**2))
            g = np.sqrt(abs(average[x][y][1]**2 - image[x][y][1]**2))
            b = np.sqrt(abs(average[x][y][2]**2 - image[x][y][2]**2))
    
            #L2 norm
            s[x][y] = int(np.sqrt((r**2 + g**2 + b**2) / 3))
            if s[x][y] > 255:
                print(s[x][y])

    cv2.imwrite('S.JPG', s)
    print("standard deviation calculated")