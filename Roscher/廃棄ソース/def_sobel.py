#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
#import matplotlib.pyplot as plt
import numpy as np
import cv2
import math

def gradient(image_name, k):
    #グレースケールに変換
    gray_image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)

    #画像サイズを取得
    height, width = gray_image.shape

    #sobel フィルタ
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize = k)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize = k)
    
    
    #勾配情報用のリスト
    G = [[[0] * 2 for i in range(width)] for j in range(height)]
    for x in range(height):
        for y in range(width):
            #勾配の大きさ
            magnitude = math.sqrt(sobel_x[x][y]**2 + sobel_y[x][y]**2)
            #if magnitude < :
            #    magnitude = 0
            #勾配の方向、atan2は引数がy,xなので注意
            direction = math.degrees(math.atan2(sobel_y[x][y], sobel_x[x][y]))

            G[x][y][0] = magnitude
            G[x][y][1] = direction
    return G