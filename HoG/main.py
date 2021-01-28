#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
#import cv2
import json
import def_resize
import def_data2
import def_HoG



resize_k = 8
#def_resize.resize(resize_k)

image_num = def_data2.create_pic(resize_k)

file_name = "cut_img"
#def_HoG.get_feature(file_name, image_num)