#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math

def center_detect(g, k):
    image = cv2.imread("B.JPG", 0)                                          #グレースケールで読み込み
    height, width = image.shape[:2]
    thr, image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
    #A = [[0] * height for i in range(width)]
    a = np.zeros((height, width),np.uint8)*255

    count = 0
    for x in range(width):
        for y in range(height):
            direction_g = math.degrees(math.atan2(g[x][y][1], g[x][y][0]))    #(y,x)なので注意
            if direction_g < 0:
                direction_g += 180                                            #0 < direction_g < 180

            for i in range(-k, k + 1):
                if image[y][x] == 0:
                    break
                for j in range(k, k + 1):
                    if x + i < 0 or width < x + i:
                        break
                    if y + j < 0 or height < y + j:
                        break
                    if (abs(i)**2) * (abs(j)**2) < 10:
                        break
                    if (abs(i)**2) * (abs(j)**2) > k**2:
                        break

                    direction_ij = math.degrees(math.atan2(j, i))
                    if direction_ij < 0:
                        direction_ij += 180
                    if abs(direction_g - direction_ij) < 10:
                        #A[x][y] += 1
                        a[y][x] += 4
    cv2.imwrite('A.JPG', a)
    print(count)