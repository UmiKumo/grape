#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict
import cv2

json_open = open("file_before.json",'r')
json_load = json.load(json_open, object_pairs_hook=OrderedDict)
data_name = json_load.keys()
data_name = "".join(data_name)
json_open.close()

p = 1
q = 1
image = cv2.imread("/disk021/share/omura/20190531/441050001033/IMG_3347.JPG")
for i in range(len(json_load[data_name][p]["points"][q]["centers"])):
    x = int(json_load[data_name][p]["points"][q]["centers"][i][0])
    y = int(json_load[data_name][p]["points"][q]["centers"][i][1])
    cv2.drawMarker(image, (x, y), (255, 0, 0), markerType=cv2.MARKER_CROSS, markerSize=20)
cv2.imwrite("test.JPG", image)