#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import json
from collections import OrderedDict
import math

json_open = open("/disk021/share/omura/grape/file_before.json",'r')
json_load = json.load(json_open, object_pairs_hook=OrderedDict)
data_name = json_load.keys()
data_name = "".join(data_name)
img_name = "resized.JPG"
img_name = "/disk021/share/omura/20190531/441050001033/IMG_3341.JPG"
x = int(json_load[data_name][0]["points"][0]["centers"][1][0])
y = int(json_load[data_name][0]["points"][0]["centers"][1][1])

image = cv2.imread("/disk021/share/omura/20190531/441050001033/IMG_3341.JPG")
x = int(json_load[data_name][0]["points"][0]["centers"][0][0])
y = int(json_load[data_name][0]["points"][0]["centers"][0][1])
cv2.drawMarker(image, (x, y), (255, 0, 0), markerType=cv2.MARKER_CROSS, markerSize=40)
cv2.imwrite("plot.JPG", image)

image = cv2.imread("resized.JPG")
x = int(json_load[data_name][0]["points"][0]["centers"][0][0] / 8)
y = int(json_load[data_name][0]["points"][0]["centers"][0][1] / 8)
cv2.drawMarker(image, (x, y), (255, 0, 0), markerType=cv2.MARKER_CROSS, markerSize=40)
cv2.imwrite("plot.JPG", image)