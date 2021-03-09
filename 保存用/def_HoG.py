#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math

def get_feature(img_name):
    win_size = (64, 64)
    block_size = (16, 16)
    block_stride = (8, 8)
    cell_size = (8, 8)
    bins = 9

    gray = cv2.imread(img_name, 0)
    gray = cv2.resize(gray, win_size)
    hog = cv2.HOGDescriptor( win_size, block_size, block_stride, cell_size, bins )
    gray = hog.compute(gray)

    return np.array(gray, np.float32)