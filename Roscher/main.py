#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import cv2
import def_resize
import def_ridge1d
import def_ridge2
import def_ridge3
import def_vote
import def_peak


#os.remove("resized.JPG")
#os.remove("S.JPG")
#os.remove("G.JPG")
#os.remove("R.JPG")
#os.remove("B.JPG")
resize_k = 8
#sobel_k = 3
ridge_k = 4
vote_k = 25
image_name = "IMG_1039.JPG"

#def_resize.resize(image_name, resize_k)
image_name = "resized.JPG"

#def_ridge1d.standard_deviation(image_name, ridge_k)

g = def_ridge2.gradient(ridge_k)

#def_ridge3.ridge(g, ridge_k)

def_vote.center_detect(g, vote_k)

def_peak.peak_detect()