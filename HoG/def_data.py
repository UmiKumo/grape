#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import json
from collections import OrderedDict
import math

def create_pic(resize_k):
    json_open = open("/disk021/share/omura/grape/file_before.json",'r')
    json_load = json.load(json_open, object_pairs_hook=OrderedDict)
    data_name = json_load.keys()
    data_name = "".join(data_name)          #list -> str

    i = 0

    #img_name = json_load[data_name][i]["images"][0]
    img_name = "resized.JPG"
    points_num = len(json_load[data_name][i]["points"][0]["centers"])

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
    
    x = int(json_load[data_name][i]["points"][0]["centers"][0][0] / resize_k)
    y = int(json_load[data_name][i]["points"][0]["centers"][0][1] / resize_k)
    radius = 0
    length = 0
    img = cv2.imread("resized.JPG")
    for i in range(len(json_load[data_name][0]["points"][0]["centers"])):
        print(i)
        for l in range(int(24 / resize_k), int(136/ resize_k)):
            signature = 0
            for w in range(36):
                p = math.cos(math.radians(10 * w))
                q = math.sin(math.radians(10 * w))
                xx = int(x + p * l)
                yy = int(y + q * l)

                if xx < 0 or width <= xx:
                    continue
                if yy < 0 or height <= yy:
                    continue

                signature += G[yy][xx]

            if signature > length:
                radius = l
                length = signature
     
        cut_img = np.zeros((radius * 2 + 3, radius * 2 + 3, 3),np.uint8)*255
        x_center = int(json_load[data_name][0]["points"][0]["centers"][i][0] / resize_k)
        y_center = int(json_load[data_name][0]["points"][0]["centers"][i][1] / resize_k)
        for a in range(radius * 2 + 3):
            for b in range(radius * 2 + 3):
                for c in range(3):
                    cut_img[b][a][c] = img[y_center - radius - 1 + b][x_center - radius - 1 + a][c]
        cut_img_name = "cut_img_" + str(i) + ".JPG"
        cv2.imwrite(cut_img_name, cut_img)

    return len(json_load[data_name][0]["points"][0]["centers"])