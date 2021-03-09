#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math

def center_detect(g, k):
    image = cv2.imread("B.JPG", 0)                                          #グレースケールで読み込み
    height, width = image.shape[:2]
    thr, image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)              #2値化
    a = np.zeros((height, width),np.uint8)*255

    for x in range(width):
        if x%100 == 0:
            print(x)
        for y in range(height):
            if image[y][x] == 0:
                continue
            direction_g = math.degrees(math.atan2(g[x][y][1], g[x][y][0]))    #(y,x)なので注意
            if direction_g < 0:
                direction_g += 180                                            #0 < direction_g < 180

            for i in range(x - k, x + k + 1):
                for j in range(y - k, y + k + 1):
                    if i < 0 or width <= i:
                        continue
                    if j < 0 or height <= j:
                        continue
                    if (abs(i - x)**2) * (abs(j - y)**2) < 10:
                        continue
                    if (abs(i - x)**2) * (abs(j - y)**2) > k**2:
                        continue

                    direction_ij = math.degrees(math.atan2(j - y, i - x))
                    if direction_ij < 0:
                        direction_ij += 180
                    if abs(direction_g - direction_ij) < 10:
                        a[j][i] += 2
    #thr, image = cv2.threshold(a, 216, 255, cv2.THRESH_BINARY)
    cv2.imwrite("A.JPG", a)
    #cv2.imwrite("test.JPG",image)