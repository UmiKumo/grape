#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math

def get_feature(file_name, image_num):
    imgs = []
    win_size = (16, 16)
    block_size = (4, 4)
    block_stride = (2, 2)
    cell_size = (2, 2)
    bins = 9
    for i in range(image_num):
        image_name = file_name + str(i) + ".JPG"
        gray = cv2.imread(image_name, 0)
        gray = cv2.resize(gray, win_size)
        hog = cv2.HOGDescriptor( win_size, block_size, block_stride, cell_size, bins )
        gray = hog.compute(gray)
        imgs.append(gray)

    return np.array(imgs, np.float32)