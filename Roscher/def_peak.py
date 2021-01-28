#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math
from scipy.ndimage.filters import maximum_filter

def peak_detect():
    image = cv2.imread("A.JPG")
    height, width = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filter_size = 3
    order = 0.7

    #https://qiita.com/yoneda88/items/0cf4a9384c1c2203ea95#2次元配列データのピーク検出の仕組み
    local_max = maximum_filter(gray, footprint=np.ones((filter_size, filter_size)), mode='constant')
    detected_peaks = np.ma.array(gray, mask=~(gray == local_max))

    temp = np.ma.array(detected_peaks, mask=~(detected_peaks >= detected_peaks.max() * order))
    peaks_index = np.where((temp.mask != True))


    coordinates = np.zeros((height, width),np.uint8)*255
    for i in range(len(peaks_index[0])):
        coordinates[peaks_index[0][i]][peaks_index[1][i]] = 255
    cv2.imwrite("coordinates.JPG", coordinates)


    image2 = cv2.imread("resized.JPG")
    print(len(peaks_index[0]))
    for i in range(len(peaks_index[0])):
        cv2.drawMarker(image, (peaks_index[1][i], peaks_index[0][i]), (0, 0, 255), markerType=cv2.MARKER_CROSS, markerSize=5)
        cv2.drawMarker(image2, (peaks_index[1][i], peaks_index[0][i]), (0, 0, 255), markerType=cv2.MARKER_CROSS, markerSize=15)
    cv2.imwrite("plot2.JPG", image)
    cv2.imwrite("plot.JPG", image2)