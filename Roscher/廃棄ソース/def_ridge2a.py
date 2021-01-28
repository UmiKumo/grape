#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
#import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import math
from decimal import Decimal, ROUND_HALF_UP

def gradient(k):
    image = cv2.imread("S.JPG")
    image = cv2.blur(image,(2*k+1, 2*k+1))
    cv2.imwrite('S_.JPG', image)
    height, width = image.shape[:2]

    image = Image.open("S_.JPG")
    image_data = image.getdata()
    g = [[[0] * 2 for i in range(height)] for j in range(width)]
    for x in range(k, width - k):
        print(x)
        for y in range(k, height - k):
            g_vector = 0.0
            for w in range(8):
                p = math.cos(math.radians(22.5 * w)) * k
                q = math.sin(math.radians(22.5 * w)) * k

                p = Decimal(str(p))
                q = Decimal(str(q))

                int_p = int(p.quantize(Decimal('0'), rounding=ROUND_HALF_UP))
                int_q = int(q.quantize(Decimal('0'), rounding=ROUND_HALF_UP))

                g_p = np.array(p, dtype='u8')
                g_q = np.array(q, dtype='u8')

                g_vector = image_data[(y + int_q) * width + (x + int_p)] - image_data[(y - int_q) * width + (x - int_p)]
                g[x][y][0] += g_vector * int_p
                g[x][y][1] += g_vector * int_q

            '''
            if g_x == 0:
                g[x][y] = 90
            else:
                g[x][y] = math.degrees(math.atan(g_y / g_x))
            '''
    
    return g