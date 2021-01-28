#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import cv2

#[[[0] * 3 for i in range(height)] for j in range(width)]   ->  width, height
#[[0] * height for i in range(width)]
#np.zeros((height, width),np.uint8)*255                     ->  height, width


x = 100
y = 100
k = 20
count = 0

image = cv2.imread("resized.JPG")
A = cv2.imread("test.JPG", 0)                                          #グレースケールで読み込み
height, width = image.shape[:2]
thr, A = cv2.threshold(A, 0, 255, cv2.THRESH_OTSU)

for x in range(width):
    for y in range(height):
        if A[y][x] > 200:
            cv2.drawMarker(image, (x, y), (255, 0, 0), markerType=cv2.MARKER_CROSS, markerSize=20)
cv2.imwrite("plot.JPG", image)