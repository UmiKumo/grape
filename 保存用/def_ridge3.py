#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math
from decimal import Decimal, ROUND_HALF_UP

def ridge(g, k):
    image = cv2.imread("G.JPG")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = image.shape[:2]
    r = np.zeros((height, width),np.uint8)*255
    b = np.zeros((height, width),np.uint8)*255

    max_B = 0
    max_R = 0
    for x in range(k, width - k):
        if x%100 == 0:
            print(x)
        for y in range(k, height - k):
            R = 0
            for w in range(8):
                p = math.cos(math.radians(22.5 * w)) * k
                q = math.sin(math.radians(22.5 * w)) * k

                p = Decimal(str(p))
                q = Decimal(str(q))

                p = int(p.quantize(Decimal('0'), rounding=ROUND_HALF_UP))
                q = int(q.quantize(Decimal('0'), rounding=ROUND_HALF_UP))

                G = -1 * int(g[x + p][y + q][0]) * int(g[x - p][y - q][0])  -  int(g[x + p][y + q][1]) * int(g[x - p][y - q][1])
                #G = -1 * int(g[y + q][x + p][0]) * int(g[y - q][x - p][0])  -  int(g[y + q][x + p][1]) * int(g[y - q][x - p][1])

                if G < 0:
                    G = 0

                G = np.sqrt(G)

                if G > R:
                    R = G
        
                r[y][x] = R / 6
                B = R - image[y][x]
                if B < 0:
                    B = 0
                b[y][x] = B / 4


    print("ridge detected")

    cv2.imwrite('R.JPG', r)
    cv2.imwrite('B.JPG', b)