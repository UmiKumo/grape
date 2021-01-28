#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math
from decimal import Decimal, ROUND_HALF_UP

def gradient(k):
    image = cv2.imread("S.JPG")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.blur(image,(2*k+1, 2*k+1))
    height, width = image.shape[:2]
    g = [[[0] * 3 for i in range(height)] for j in range(width)]    #(x, y, length=strength)
    G = np.zeros((height, width),np.uint8)*255

    max_gradient = 0
    for x in range(k, width - k):
        if x%100 == 0:
            print(x)
        for y in range(k, height - k):
            for w in range(8):
                p = math.cos(math.radians(22.5 * w)) * k
                q = math.sin(math.radians(22.5 * w)) * k

                p = Decimal(str(p))
                q = Decimal(str(q))

                p = int(p.quantize(Decimal('0'), rounding=ROUND_HALF_UP))
                q = int(q.quantize(Decimal('0'), rounding=ROUND_HALF_UP))

                g_vector = int(image[y + q][x + p]) - int(image[y - q][x - p])
                g[x][y][0] += g_vector * p
                g[x][y][1] += g_vector * q
            g[x][y][2] = math.sqrt(g[x][y][0]**2 + g[x][y][1]**2)
            if max_gradient < g[x][y][2]:
                max_gradient = g[x][y][2]

    for x in range(k, width - k):
        for y in range(k, height - k):
            G[y][x] = g[x][y][2] * 255 / max_gradient

    cv2.imwrite('G.JPG', G)
    print("gradient calculated")
    return g