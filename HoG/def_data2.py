#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math

def create_pic(resize_k):
    img_name = "resized.JPG"
    gray_image = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    height, width = gray_image.shape
    k = 3
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize = k)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize = k)
    G = np.zeros((height, width),np.uint8)*255
    for x in range(width):
        if x%100 == 0:
            print(x)
        for y in range(height):
            #勾配の大きさ
            G[y][x] = math.sqrt(sobel_x[y][x]**2 + sobel_y[y][x]**2)

    
    x_center = []
    y_center = []
    coordinates = cv2.imread("coordinates_1039.JPG", cv2.IMREAD_GRAYSCALE)
    ret, coordinates = cv2.threshold(coordinates, 150, 255, cv2.THRESH_BINARY)
    for i in range(width):
        for j in range(height):
            if coordinates[j][i] == 255:
                x_center.append(i)
                y_center.append(j)


    
    radius = 0
    length = 0
    img = cv2.imread("resized.JPG")
    for i in range(len(x_center)):
        for l in range(3, 20):                              #決め打ち
            signature = 0
            for w in range(16):
                p = math.cos(math.radians(22.5 * w))
                q = math.sin(math.radians(22.5 * w))
                xx = int(x_center[i] + p * l)
                yy = int(y_center[i] + q * l)

                if xx < 0 or width <= xx:
                    continue
                if yy < 0 or height <= yy:
                    continue

                signature += G[yy][xx]

            if signature > length:
                radius = l
                length = signature
     
        cut_img = np.zeros((radius * 2 + 3, radius * 2 + 3, 3),np.uint8)*255
        for a in range(radius * 2 + 3):
            for b in range(radius * 2 + 3):
                for c in range(3):
                    cut_img[b][a][c] = img[y_center[i] - radius - 1 + b][x_center[i] - radius - 1 + a][c]
        cut_img_name = "cut_img_" + str(i) + ".JPG"
        cv2.imwrite(cut_img_name, cut_img)

    return len(x_center)